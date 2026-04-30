import os
from pathlib import Path
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class BuildAsset(BaseModel):
    """Metadata about a generated build artifact."""
    output_path: str
    domain: str
    language: str
    timestamp: datetime = datetime.now()

class BuildManager:
    """Coordinates directory structure and path generation for the build/ directory."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.build_dir = project_root / "build"

    def get_output_path(self, domain: str, language: str, filename: str) -> Path:
        """Generates a hierarchical path: build/<domain>/<language>/<filename>."""
        # Security: Prevent directory traversal in domain or language
        if ".." in domain or ".." in language or ".." in filename:
            raise ValueError("Security violation: Path components cannot contain '..'")
            
        target_dir = self.build_dir / domain / language
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir / filename

    def resolve_template_path(self, template_path: str) -> Path:
        """Resolves a template path relative to the templates/ directory."""
        full_path = (self.project_root / "templates" / template_path).resolve()
        if not str(full_path).startswith(str((self.project_root / "templates").resolve())):
            raise ValueError("Security violation: Template must be within the templates/ directory.")
        return full_path
