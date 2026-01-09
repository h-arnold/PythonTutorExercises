"""Exercise selector."""

from __future__ import annotations

from pathlib import Path


class ExerciseSelector:
    """Select exercises based on various criteria."""

    def __init__(self, repo_root: Path):
        """Initialize selector."""
        self.repo_root = repo_root

    def select_by_construct(self, constructs: list[str]) -> list[str]:
        """Select exercises by construct."""
        raise NotImplementedError("Not yet implemented")

    def select_by_type(self, types: list[str]) -> list[str]:
        """Select exercises by type."""
        raise NotImplementedError("Not yet implemented")

    def select_by_construct_and_type(
        self, constructs: list[str], types: list[str]
    ) -> list[str]:
        """Select exercises by construct AND type."""
        raise NotImplementedError("Not yet implemented")

    def select_by_notebooks(self, notebooks: list[str]) -> list[str]:
        """Select specific notebooks."""
        raise NotImplementedError("Not yet implemented")

    def select_by_pattern(self, pattern: str) -> list[str]:
        """Select notebooks by pattern."""
        raise NotImplementedError("Not yet implemented")
