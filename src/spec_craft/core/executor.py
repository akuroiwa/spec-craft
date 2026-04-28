import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional

class ScriptExecutor:
    """Safely executes spec-kit tactical scripts."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.scripts_dir = project_root / ".specify" / "scripts" / "bash"

    def execute(self, script_name: str, args: Optional[List[str]] = None) -> Dict[str, Any]:
        """Executes a script and returns the output."""
        script_path = (self.scripts_dir / script_name).resolve()
        
        # Security: Ensure the script is within the allowed directory
        if not str(script_path).startswith(str(self.scripts_dir.resolve())):
            raise ValueError(f"Security violation: Script must be within {self.scripts_dir}")
        
        if not script_path.is_file():
            raise FileNotFoundError(f"Tactical script not found: {script_path}")

        command = ["bash", str(script_path)] + (args or [])
        
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=str(self.project_root),
                check=False
            )
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode,
                "command": " ".join(command)
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": str(e),
                "exit_code": 1,
                "command": " ".join(command)
            }
