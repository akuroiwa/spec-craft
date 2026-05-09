from pathlib import Path
from typing import Dict, Any, List

class BonsaiDriver:
    """Handles generation of Bonsai (BlenderBIM) Python scripts for architectural modeling."""

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def generate_ifc_script(self, scene_spec: Dict[str, Any], output_path: Path) -> Path:
        """Generates a .py script for Bonsai architectural construction."""
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Build the script content targeting the official Bonsai (BlenderBIM) API
        script_lines = [
            "import bpy",
            "import bonsai.operators",
            "from bonsai.bim.ifc import IfcStore",
            "",
            "def setup_project():",
            "    # Initialize a new IFC project if none exists",
            "    if not IfcStore.get_file():",
            "        bpy.ops.bim.create_project()",
            "",
            "def create_wall(name, location):",
            "    # Correct Bonsai wall creation pattern verified from research",
            "    bpy.ops.bim.add_container(type='IfcWall')",
            "    wall = bpy.context.active_object",
            "    wall.name = name",
            "    wall.location = location",
            "    # Assign specific IFC attributes if needed",
            "",
            "def run_architecture():",
            "    setup_project()",
            ""
        ]
        
        # Add elements from spec
        for element in scene_spec.get("elements", []):
            etype = element.get("type")
            name = element.get("name", etype)
            pos = element.get("position", (0, 0, 0))
            if etype == "wall":
                script_lines.append(f"    create_wall('{name}', {pos})")
            elif etype == "slab":
                script_lines.append(f"    # Logic for IfcSlab creation")

        script_lines.extend([
            "",
            "if __name__ == '__main__':",
            "    run_architecture()"
        ])

        output_path.write_text("\n".join(script_lines))
        return output_path
