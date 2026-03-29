"""Unified AI client wrapper supporting OpenAI and Anthropic."""

import os
import time
import logging
from typing import Optional

from .config_loader import get_config, load_env

logger = logging.getLogger(__name__)


class AIClient:
    """Unified interface for AI text generation.

    Supports OpenAI and Anthropic behind a single generate() method.
    Handles retries, rate limiting, and provider switching.
    """

    def __init__(self, module_name: Optional[str] = None):
        load_env()
        config = get_config(module_name)
        ai_config = config.get("ai", config) if "ai" in config else config

        self.provider = ai_config.get("provider", os.getenv("AI_PROVIDER", "openai"))
        self.model = ai_config.get("model", os.getenv("AI_MODEL", "gpt-4o-mini"))
        self.temperature = float(ai_config.get("temperature", 0.7))
        self.max_tokens = int(ai_config.get("max_tokens", 2000))
        self.max_retries = 3
        self._client = None

    def _get_client(self):
        """Lazy-initialize the appropriate client."""
        if self._client is not None:
            return self._client

        if self.provider == "openai":
            from openai import OpenAI
            self._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        elif self.provider == "anthropic":
            import anthropic
            self._client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

        return self._client

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        model: Optional[str] = None,
    ) -> str:
        """Generate text using the configured AI provider.

        Args:
            prompt: The user prompt/message
            system_prompt: Optional system instruction
            temperature: Override default temperature
            max_tokens: Override default max tokens
            model: Override default model

        Returns:
            Generated text string
        """
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens
        mdl = model or self.model

        for attempt in range(self.max_retries):
            try:
                if self.provider == "openai":
                    return self._generate_openai(prompt, system_prompt, temp, tokens, mdl)
                elif self.provider == "anthropic":
                    return self._generate_anthropic(prompt, system_prompt, temp, tokens, mdl)
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{self.max_retries} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    raise

    def _generate_openai(self, prompt, system_prompt, temperature, max_tokens, model):
        client = self._get_client()
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    def _generate_anthropic(self, prompt, system_prompt, temperature, max_tokens, model):
        client = self._get_client()
        kwargs = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system_prompt:
            kwargs["system"] = system_prompt

        response = client.messages.create(**kwargs)
        return response.content[0].text

    def generate_structured(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        sections: Optional[list] = None,
    ) -> dict:
        """Generate text and parse it into sections.

        Useful for generating structured content like blog posts with
        title, intro, body, conclusion, etc.
        """
        if sections:
            section_list = "\n".join(f"## {s}" for s in sections)
            structured_prompt = (
                f"{prompt}\n\n"
                f"Structure your response with these exact section headers:\n{section_list}"
            )
        else:
            structured_prompt = prompt

        raw = self.generate(structured_prompt, system_prompt)

        if not sections:
            return {"content": raw}

        result = {}
        current_section = None
        current_content = []

        for line in raw.split("\n"):
            stripped = line.strip()
            if stripped.startswith("## "):
                if current_section:
                    result[current_section] = "\n".join(current_content).strip()
                current_section = stripped[3:].strip()
                current_content = []
            elif current_section:
                current_content.append(line)

        if current_section:
            result[current_section] = "\n".join(current_content).strip()

        return result
