import pytest
from pathlib import Path
from spec_craft.core.drivers.blender import BlenderDriver

def test_blender_generate_script(temp_workspace):
    """Verify that BlenderDriver generates a valid Python script."""
    driver = BlenderDriver(temp_workspace)
    
    scene_spec = {
        "width": 15,
        "depth": 15,
        "elements": [
            {"type": "mountain", "position": (2, 3, 0)},
            {"type": "tree", "position": (-1, -1, 0)}
        ]
    }
    
    output_path = temp_workspace / "build" / "3d" / "scene.py"
    driver.generate_script(scene_spec, output_path)
    
    assert output_path.is_file()
    content = output_path.read_text()
    
    assert "import bpy" in content
    assert "create_bonkei_base(15, 15)" in content
    assert "primitive_cone_add" in content
    assert "primitive_cylinder_add" in content
    assert "location=(2, 3, 0)" in content
