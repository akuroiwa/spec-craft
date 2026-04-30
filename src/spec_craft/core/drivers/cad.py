import subprocess
from pathlib import Path
from typing import Dict, Any

class CADDriver:
    """Handles JSCAD code execution and STL generation."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        # Assume jscad-tool.js is in the project root as per gemini-jscad patterns
        self.jscad_tool = project_root / "jscad-tool.js"

    def build_stl(self, jscad_code: str, output_path: Path):
        """Saves JSCAD code and converts it to STL."""
        # Ensure directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save .js source
        js_path = output_path.with_suffix(".js")
        js_path.write_text(jscad_code)
        
        if not self.jscad_tool.is_file():
            # In a real environment, this tool must exist.
            # For this MVP, we report the missing tool if not found.
            raise FileNotFoundError(f"jscad-tool.js not found at {self.jscad_tool}. Please ensure it is present in the project root.")

        command = ["node", str(self.jscad_tool), str(js_path), "-o", str(output_path)]
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"JSCAD build failed: {result.stderr}")
        
        return output_path
