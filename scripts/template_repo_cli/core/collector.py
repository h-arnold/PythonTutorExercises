"""File collector."""

from __future__ import annotations

from pathlib import Path


class FileCollector:
    """Collect files for exercises."""

    def __init__(self, repo_root: Path):
        """Initialize collector."""
        self.repo_root = repo_root

    def collect_files(self, exercise_id: str) -> dict[str, Path]:
        """Collect all files for an exercise."""
        raise NotImplementedError("Not yet implemented")

    def collect_multiple(self, exercise_ids: list[str]) -> dict[str, dict[str, Path]]:
        """Collect files for multiple exercises."""
        raise NotImplementedError("Not yet implemented")
