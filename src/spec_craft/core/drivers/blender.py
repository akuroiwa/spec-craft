from pathlib import Path
from typing import Dict, Any

class BlenderDriver:
    """Handles generation of Blender Python scripts (bpy)."""

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def generate_script(self, scene_spec: Dict[str, Any], output_path: Path, enable_svg: bool = False) -> Path:
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
            "def setup_freestyle(output_file):",
            "    # Enable Freestyle and SVG exporter",
            "    bpy.ops.preferences.addon_enable(module='render_freestyle_svg')",
            "    scene = bpy.context.scene",
            "    scene.render.use_freestyle = True",
            "    scene.svg_export.use_svg_export = True",
            "    scene.render.filepath = output_file",
            "",
            "def create_bonkei_base(width, depth):",
            "    bpy.ops.mesh.primitive_cube_add(size=1, scale=(width, depth, 0.1))",
            "    base = bpy.context.active_object",
            "    base.name = 'BonkeiBase'",
            ""
        ]
        
        # Add construction logic header
        svg_filename = output_path.with_suffix(".svg").name
        script_lines.extend([
            "def run_construction():",
            "    clear_scene()",
            f"    create_bonkei_base({scene_spec.get('width', 10)}, {scene_spec.get('depth', 10)})"
        ])

        # Add elements from spec
        for element in scene_spec.get("elements", []):
            etype = element.get("type")
            pos = element.get("position", (0, 0, 0))
            if etype == "mountain":
                script_lines.append(f"    bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location={pos})")
            elif etype == "tree":
                script_lines.append(f"    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=1, location={pos})")

        if enable_svg:
            script_lines.append(f"    setup_freestyle('{svg_filename}')")
            # Note: Final render call to produce SVG
            script_lines.append("    bpy.ops.render.render(write_still=True)")

        script_lines.extend([
            "",
            "if __name__ == '__main__':",
            "    run_construction()"
        ])

        output_path.write_text("\n".join(script_lines))
        return output_path

    def render_svg(self, script_path: Path, output_svg_path: Path) -> Path:
        """Executes a Blender script headlessly to generate an SVG render."""
        import subprocess
        
        # Ensure output directory exists
        output_svg_path.parent.mkdir(parents=True, exist_ok=True)
        
        command = [
            "blender",
            "-b",  # Headless
            "-P", str(script_path)
        ]
        
        try:
            subprocess.run(command, check=True, capture_output=True, text=True, cwd=str(self.project_root))
            
            # Note: The script itself handles the SVG path, but we verify here
            if not output_svg_path.is_file():
                # Blender might output to the CWD if not careful, check there
                potential_output = self.project_root / output_svg_path.name
                if potential_output.is_file():
                    potential_output.rename(output_svg_path)
            
            if not output_svg_path.is_file():
                raise FileNotFoundError(f"Blender failed to produce SVG at {output_svg_path}")
                
            return output_svg_path
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Blender render failed: {e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("Blender executable not found. Please install Blender and ensure it is in your PATH.")
