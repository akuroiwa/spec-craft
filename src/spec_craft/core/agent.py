from pathlib import Path
from typing import List, Optional
import yaml
from pydantic import BaseModel

class ExtensionInfo(BaseModel):
    """Metadata about a specific agent extension and its installation status."""
    name: str
    is_installed: bool
    install_command: Optional[str] = None

class AgentManager:
    """Manages detection of agent extensions and capabilities by inspecting .specify configuration."""

    def __init__(self, project_root: Path):
        """Initializes the AgentManager with the project root path."""
        self.project_root = project_root
        self.extensions_file = project_root / ".specify" / "extensions.yml"

    def get_extension_status(self, required_extensions: List[str]) -> List[ExtensionInfo]:
        """Checks which extensions are currently registered in .specify/extensions.yml."""
        installed_extensions = self._load_registered_extensions()
        
        status = []
        for ext in required_extensions:
            is_installed = ext in installed_extensions
            install_cmd = f"gemini-cli extension install {ext}" if not is_installed else None
            status.append(ExtensionInfo(
                name=ext,
                is_installed=is_installed,
                install_command=install_cmd
            ))
        return status

    def _load_registered_extensions(self) -> List[str]:
        """Loads the list of installed extensions from the config file."""
        if not self.extensions_file.is_file():
            return []
        
        try:
            data = yaml.safe_load(self.extensions_file.read_text())
            # Based on the sample provided in previous turns:
            # installed: [ {extension: 'git', ...} ]
            installed_data = data.get("installed", [])
            return [item.get("extension") for item in installed_data if isinstance(item, dict) and "extension" in item]
        except (yaml.YAMLError, AttributeError):
            return []
