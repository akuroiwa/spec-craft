from pathlib import Path
from typing import Dict, Any

class BlenderDriver:
    """Handles generation of Blender Python scripts (bpy)."""

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def generate_script(self, scene_spec: Dict[str, Any], output_path: Path) -> Path:
        """Generates a .py script for Blender scene construction."""
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Build the script content
        script_lines = [
            "import bpy",
            "import bmesh",
            "",
            "def clear_scene():",
            "    bpy.ops.object.select_all(action='SELECT')",
            "    bpy.ops.object.delete()",
            "",
            "def create_bonkei_base(width, depth):",
            "    bpy.ops.mesh.primitive_cube_add(size=1, scale=(width, depth, 0.1))",
            "    base = bpy.context.active_object",
            "    base.name = 'BonkeiBase'",
            "",
            "def run_construction():",
            "    clear_scene()",
            f"    create_bonkei_base({scene_spec.get('width', 10)}, {scene_spec.get('depth', 10)})",
            ""
        ]
        
        # Add elements from spec
        for element in scene_spec.get("elements", []):
            etype = element.get("type")
            pos = element.get("position", (0, 0, 0))
            if etype == "mountain":
                script_lines.append(f"    bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location={pos})")
            elif etype == "tree":
                script_lines.append(f"    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=1, location={pos})")

        script_lines.extend([
            "",
            "if __name__ == '__main__':",
            "    run_construction()"
        ])

        output_path.write_text("\n".join(script_lines))
        return output_path
