"""Shared utility functions for all modules."""

import json
import os
import re
from datetime import datetime
from pathlib import Path


def save_output(content: str, filename: str, output_dir: str = "output") -> str:
    """Save generated content to a file.

    Returns the full path of the saved file.
    """
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    filepath = path / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return str(filepath)


def save_json(data: dict, filename: str, output_dir: str = "output") -> str:
    """Save data as JSON file."""
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    filepath = path / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return str(filepath)


def timestamp_filename(base_name: str, ext: str = "md") -> str:
    """Generate a timestamped filename."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = slugify(base_name)
    return f"{safe_name}_{ts}.{ext}"


def slugify(text: str) -> str:
    """Convert text to a URL/filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80]


def word_count(text: str) -> int:
    """Count words in text (supports Arabic and English)."""
    return len(text.split())


def truncate(text: str, max_length: int = 200, suffix: str = "...") -> str:
    """Truncate text to max_length characters."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def read_template(template_path: str) -> str:
    """Read a template file and return its content."""
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def format_template(template: str, **kwargs) -> str:
    """Format a template string with the given variables."""
    return template.format(**kwargs)


def ensure_dir(path: str) -> Path:
    """Ensure a directory exists and return its Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
