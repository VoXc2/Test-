"""Central configuration loader for all modules."""

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

_config_cache = None
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def load_env():
    """Load environment variables from .env file."""
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    else:
        load_dotenv(PROJECT_ROOT / ".env.example")


def _load_yaml_config():
    """Load and cache the YAML configuration."""
    global _config_cache
    if _config_cache is None:
        config_path = PROJECT_ROOT / "config" / "settings.yaml"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                _config_cache = yaml.safe_load(f) or {}
        else:
            _config_cache = {}
    return _config_cache


def get_config(module_name=None):
    """Get configuration for a specific module or the full config.

    Args:
        module_name: Optional module name (e.g., 'content_generation', 'translation_service')

    Returns:
        dict with merged configuration
    """
    load_env()
    config = _load_yaml_config()

    if module_name is None:
        return config

    # Get module-specific config
    module_config = config.get(module_name, {})

    # Merge with AI defaults + any AI overrides for this module
    ai_config = config.get("ai", {})
    ai_overrides = ai_config.get("overrides", {}).get(module_name, {})

    merged_ai = {
        "provider": os.getenv("AI_PROVIDER", ai_config.get("default_provider", "openai")),
        "model": os.getenv("AI_MODEL", ai_config.get("default_model", "gpt-4o-mini")),
        "temperature": float(os.getenv("AI_TEMPERATURE", ai_config.get("temperature", 0.7))),
        "max_tokens": int(os.getenv("AI_MAX_TOKENS", ai_config.get("max_tokens", 2000))),
    }
    # Apply module-specific overrides
    merged_ai.update(ai_overrides)

    return {
        "ai": merged_ai,
        **module_config,
    }


def get_output_dir(subdir=None):
    """Get output directory path, creating it if needed."""
    config = _load_yaml_config()
    output_config = config.get("output", {})
    base = PROJECT_ROOT / output_config.get("base_dir", "output")

    if subdir:
        path = PROJECT_ROOT / output_config.get(f"{subdir}_dir", f"output/{subdir}")
    else:
        path = base

    path.mkdir(parents=True, exist_ok=True)
    return path
