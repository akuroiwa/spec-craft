import os
from pathlib import Path
from typing import Optional
import git

class WorkspaceDetector:
    """Detects and provides metadata about the project workspace."""

    def __init__(self, start_path: Optional[Path] = None):
        self.root_path = start_path or Path.cwd()
        self._repo: Optional[git.Repo] = None
        self._detect_root()

    def _detect_root(self):
        """Identifies the project root by looking for .git or .specify."""
        # Try to find git root
        try:
            self._repo = git.Repo(self.root_path, search_parent_directories=True)
            self.root_path = Path(self._repo.working_tree_dir)
        except git.InvalidGitRepositoryError:
            # Fallback: look for .specify directory up the tree
            current = self.root_path.resolve()
            while current != current.parent:
                if (current / ".specify").is_dir():
                    self.root_path = current
                    return
                current = current.parent

    @property
    def is_git_repo(self) -> bool:
        return self._repo is not None

    @property
    def obsidian_path(self) -> Optional[Path]:
        path = self.root_path / "obsidian"
        return path if path.is_dir() else None

    @property
    def specify_path(self) -> Optional[Path]:
        path = self.root_path / ".specify"
        return path if path.is_dir() else None

    def get_metadata(self) -> dict:
        return {
            "root_path": str(self.root_path),
            "is_git_repo": self.is_git_repo,
            "obsidian_path": str(self.obsidian_path) if self.obsidian_path else None,
            "specify_path": str(self.specify_path) if self.specify_path else None,
        }
