"""Prompt Library Manager.

Manages the prompt inventory: load, search, preview, and execute prompts.
"""

from pathlib import Path
from typing import Optional

import yaml

from income_streams.common import AIClient
from income_streams.common.utils import truncate


class PromptManager:
    """Manage the prompt library for the marketplace."""

    def __init__(self):
        self.prompts_dir = Path(__file__).parent / "prompts"
        self.client = AIClient()
        self._catalog = None

    def _load_catalog(self) -> list:
        """Load all prompts from YAML files."""
        if self._catalog is not None:
            return self._catalog

        self._catalog = []
        for yaml_file in sorted(self.prompts_dir.glob("*.yaml")):
            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}

            category = data.get("category", yaml_file.stem)
            category_ar = data.get("category_ar", category)

            for prompt_data in data.get("prompts", []):
                prompt_data["category"] = category
                prompt_data["category_ar"] = category_ar
                self._catalog.append(prompt_data)

        return self._catalog

    def list_all(self) -> list:
        """List all available prompts."""
        return self._load_catalog()

    def list_by_category(self, category: str) -> list:
        """List prompts in a specific category."""
        return [p for p in self._load_catalog() if p["category"] == category]

    def search(self, query: str) -> list:
        """Search prompts by name or description."""
        query_lower = query.lower()
        return [
            p for p in self._load_catalog()
            if query_lower in p.get("name", "").lower()
            or query_lower in p.get("description", "").lower()
            or query_lower in p.get("name_ar", "").lower()
        ]

    def get_prompt(self, name: str) -> Optional[dict]:
        """Get a specific prompt by name."""
        for p in self._load_catalog():
            if p["name"] == name or p.get("name_ar") == name:
                return p
        return None

    def preview(self, name: str, preview_length: int = 200) -> Optional[str]:
        """Get a preview of a prompt (for marketplace display)."""
        prompt = self.get_prompt(name)
        if not prompt:
            return None
        return truncate(prompt.get("prompt", ""), preview_length)

    def execute(self, name: str, variables: dict) -> str:
        """Execute a prompt with given variables.

        Args:
            name: Prompt name
            variables: Dict of variable values

        Returns:
            AI-generated result
        """
        prompt_data = self.get_prompt(name)
        if not prompt_data:
            raise ValueError(f"Prompt not found: {name}")

        prompt_text = prompt_data["prompt"]
        for key, value in variables.items():
            prompt_text = prompt_text.replace(f"{{{key}}}", str(value))

        return self.client.generate(prompt_text, max_tokens=3000)

    def get_categories(self) -> list:
        """Get all unique categories."""
        cats = set()
        for p in self._load_catalog():
            cats.add((p["category"], p.get("category_ar", p["category"])))
        return sorted(cats)

    def get_stats(self) -> dict:
        """Get catalog statistics."""
        catalog = self._load_catalog()
        categories = {}
        for p in catalog:
            cat = p["category"]
            categories[cat] = categories.get(cat, 0) + 1

        return {
            "total_prompts": len(catalog),
            "categories": categories,
            "price_tiers": {
                "standard": len([p for p in catalog if p.get("price_tier") == "standard"]),
                "premium": len([p for p in catalog if p.get("price_tier") == "premium"]),
            },
        }
