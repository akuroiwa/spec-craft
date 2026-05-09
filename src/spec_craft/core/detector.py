import os
from pathlib import Path
from typing import Optional, List
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

    def check_environment(self) -> List[dict]:
        """Detects missing prerequisites for the Spec-Craft pipeline."""
        import shutil
        import importlib.util

        status = []

        # 1. spec-kit
        has_speckit = shutil.which("speckit") is not None or (self.root_path / ".specify").is_dir()
        status.append({
            "tool_name": "spec-kit",
            "is_installed": bool(has_speckit),
            "install_command": "pip install spec-kit" if not has_speckit else None
        })

        # 2. obsidian
        has_obsidian = self.obsidian_path is not None
        status.append({
            "tool_name": "obsidian",
            "is_installed": has_obsidian,
            "install_command": f"mkdir -p {self.root_path}/obsidian" if not has_obsidian else None
        })

        # 3. node/npx
        has_npx = shutil.which("npx") is not None
        jscad_installed = (self.root_path / "node_modules" / "@jscad" / "cli").is_dir()
        
        status.append({
            "tool_name": "node/npx",
            "is_installed": has_npx,
            "install_command": "Visit https://nodejs.org/ to install Node.js and npx" if not has_npx else None
        })
        
        status.append({
            "tool_name": "@jscad/cli",
            "is_installed": jscad_installed,
            "install_command": "npm install @jscad/cli @jscad/modeling" if not jscad_installed else None
        })

        # 4. uv
...
            "install_command": "curl -LsSf https://astral.sh/uv/install.sh | sh" if not has_uv else None
        })

        # 5. Blender Bonsai
        # Detecting Blender add-ons usually requires running blender, 
        # but we can check for common installation paths or assume manual check.
        status.append({
            "tool_name": "Bonsai (BlenderBIM)",
            "is_installed": False,  # Placeholder for manual/scripted check
            "install_command": "Visit https://bonsai-bim.org/ to install the Blender add-on"
        })

        return status
