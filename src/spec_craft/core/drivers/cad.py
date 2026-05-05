import subprocess
import os
from pathlib import Path
from typing import Dict, Any, List, Optional

class CADDriver:
    """Handles JSCAD code execution and asset generation (STL, SVG)."""

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def build(self, jscad_code: str, output_base_path: Path, formats: List[str]) -> Dict[str, Path]:
        """Saves JSCAD code and generates requested formats (stl, svg)."""
        # Ensure directory exists
        output_base_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save .js source (required for JSCAD CLI)
        js_path = output_base_path.with_suffix(".js")
        js_path.write_text(jscad_code)
        
        results = {}
        
        for fmt in formats:
            out_file = output_base_path.with_suffix(f".{fmt}")
            
            # Construct npx @jscad/cli command
            # Using --output to specify format and destination
            command = ["npx", "@jscad/cli", str(js_path), "--output", str(out_file)]
            
            # For SVG, we might want to specify a projection if needed, 
            # but standard export works for 3D -> 2D projection in many cases.
            
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    cwd=str(self.project_root),
                    check=True
                )
                results[fmt] = out_file
            except FileNotFoundError:
                raise RuntimeError("Node.js or npx not found. Please ensure Node.js is installed and npx is in your PATH.")
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"JSCAD {fmt.upper()} build failed: {e.stderr}")

        return results

    def build_stl(self, jscad_code: str, output_path: Path):
        """Legacy compatibility method for STL-only builds."""
        self.build(jscad_code, output_path.with_suffix(""), ["stl"])
        return output_path
