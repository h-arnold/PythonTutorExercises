"""Configuration utilities for template_repo_cli."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class TemplateRepoConfig:
    """Configuration settings for the CLI.

    This is intentionally minimal and uses a JSON file for storage to
    avoid external dependencies.
    """

    defaults: dict[str, Any] = field(default_factory=dict)


def default_config_path() -> Path:
    """Return the default config path in the user's home directory."""
    return Path.home() / ".template_repo_cli.json"


def load_config(path: Path | None = None) -> TemplateRepoConfig:
    """Load configuration from disk.

    Args:
        path: Optional custom config path.

    Returns:
        TemplateRepoConfig with loaded defaults (empty if missing).
    """
    config_path = path or default_config_path()
    if not config_path.exists():
        return TemplateRepoConfig()

    data = json.loads(config_path.read_text())
    if not isinstance(data, dict):
        return TemplateRepoConfig()

    return TemplateRepoConfig(defaults=data)


def save_config(config: TemplateRepoConfig, path: Path | None = None) -> None:
    """Save configuration to disk.

    Args:
        config: Configuration object to save.
        path: Optional custom config path.
    """
    config_path = path or default_config_path()
    config_path.write_text(json.dumps(config.defaults, indent=2))
