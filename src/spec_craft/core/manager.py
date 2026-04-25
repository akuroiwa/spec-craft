from pathlib import Path
from typing import Optional
from .detector import WorkspaceDetector

class ConstitutionManager:
    """Manages interactions with the .specify/memory/constitution.md file."""

    def __init__(self, detector: WorkspaceDetector):
        self.detector = detector
        self.constitution_path = self._resolve_path()

    def _resolve_path(self) -> Optional[Path]:
        """Resolves the path to the constitution file."""
        if not self.detector.specify_path:
            return None
        
        path = self.detector.specify_path / "memory" / "constitution.md"
        return path if path.is_file() else None

    def read_constitution(self) -> Optional[str]:
        """Reads the content of the constitution file."""
        if not self.constitution_path:
            return None
        
        return self.constitution_path.read_text()

    def append_rule(self, rule_title: str, rule_content: str):
        """Appends a new rule to the constitution."""
        if not self.constitution_path:
            raise FileNotFoundError("Constitution file not found.")
        
        with self.constitution_path.open("a") as f:
            f.write(f"\n### {rule_title}\n{rule_content}\n")
