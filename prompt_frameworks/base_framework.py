"""Base class for all prompt frameworks."""

import os
from abc import ABC, abstractmethod
from pathlib import Path

import yaml

from income_streams.common import AIClient


class BaseFramework(ABC):
    """Abstract base for the 14 prompt frameworks.

    Each framework loads its template from a YAML file, collects user inputs,
    builds the final prompt, and runs it through the AI client.
    """

    name: str = ""
    name_ar: str = ""
    description: str = ""
    description_ar: str = ""

    def __init__(self):
        self.client = AIClient(module_name="prompt_frameworks")
        self.template = self._load_template()

    def _load_template(self) -> dict:
        """Load the YAML template for this framework."""
        template_dir = Path(__file__).parent / "templates"
        # Derive filename from class: CareerSurvivalScanner -> career_survival_scanner.yaml
        class_name = self.__class__.__name__
        filename = ""
        for i, ch in enumerate(class_name):
            if ch.isupper() and i > 0:
                filename += "_"
            filename += ch.lower()
        filepath = template_dir / f"{filename}.yaml"

        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        return {}

    @abstractmethod
    def get_required_inputs(self) -> list:
        """Return list of required input field names."""
        ...

    def build_prompt(self, inputs: dict) -> tuple:
        """Build system and user prompts from template + inputs.

        Returns:
            (system_prompt, user_prompt) tuple
        """
        system_prompt = self.template.get("system_prompt", "")
        user_template = self.template.get("user_prompt_template", "")

        # Replace placeholders
        user_prompt = user_template
        for key, value in inputs.items():
            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)
            user_prompt = user_prompt.replace(f"{{{key}}}", str(value))

        return system_prompt, user_prompt

    def run(self, **inputs) -> str:
        """Execute the framework with given inputs.

        Args:
            **inputs: Key-value pairs matching get_required_inputs()

        Returns:
            AI-generated analysis/response
        """
        # Validate inputs
        missing = [f for f in self.get_required_inputs() if f not in inputs]
        if missing:
            raise ValueError(f"Missing required inputs: {missing}")

        system_prompt, user_prompt = self.build_prompt(inputs)
        return self.client.generate(
            prompt=user_prompt,
            system_prompt=system_prompt,
            max_tokens=4000,
        )

    def info(self) -> dict:
        """Return framework metadata."""
        return {
            "name": self.name,
            "name_ar": self.name_ar,
            "description": self.description,
            "description_ar": self.description_ar,
            "required_inputs": self.get_required_inputs(),
        }
