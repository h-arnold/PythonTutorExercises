"""GitHub operations."""

from __future__ import annotations

import json
from pathlib import Path


class GitHubClient:
    """GitHub operations client."""

    def __init__(self, dry_run: bool = False):
        """Initialize GitHub client."""
        self.dry_run = dry_run

    def build_create_command(
        self,
        repo_name: str,
        public: bool = True,
        template: bool = True,
        org: str | None = None,
        description: str | None = None,
    ) -> list[str]:
        """Build gh repo create command."""
        raise NotImplementedError("Not yet implemented")

    def execute_command(self, cmd: list[str]) -> dict[str, any]:
        """Execute a gh command."""
        raise NotImplementedError("Not yet implemented")

    def check_gh_installed(self) -> bool:
        """Check if gh CLI is installed."""
        raise NotImplementedError("Not yet implemented")

    def check_authentication(self) -> bool:
        """Check gh authentication status."""
        raise NotImplementedError("Not yet implemented")

    def parse_json_output(self, output: str) -> dict:
        """Parse JSON output from gh."""
        raise NotImplementedError("Not yet implemented")

    def create_repository(
        self, repo_name: str, workspace: Path, push: bool = False
    ) -> dict[str, any]:
        """Create a GitHub repository."""
        raise NotImplementedError("Not yet implemented")

    def init_git_repo(self, workspace: Path) -> None:
        """Initialize git repository."""
        raise NotImplementedError("Not yet implemented")

    def commit_files(self, workspace: Path, message: str) -> None:
        """Commit files."""
        raise NotImplementedError("Not yet implemented")

    def push_to_remote(self, workspace: Path, remote_url: str) -> None:
        """Push to remote."""
        raise NotImplementedError("Not yet implemented")
