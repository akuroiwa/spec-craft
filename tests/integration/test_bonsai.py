import pytest
from pathlib import Path
from spec_craft.core.drivers.bonsai import BonsaiDriver

def test_bonsai_driver_generates_ifc_script(temp_workspace):
    """Verify that BonsaiDriver generates a valid IFC script."""
    driver = BonsaiDriver(temp_workspace)
    
    scene_spec = {
        "elements": [
            {"type": "wall", "name": "MainWall", "position": (0, 0, 0)},
            {"type": "slab", "name": "Floor", "position": (0, 0, -0.3)}
        ]
    }
    
    output_path = temp_workspace / "build" / "bonsai" / "house.py"
    driver.generate_ifc_script(scene_spec, output_path)
    
    assert output_path.is_file()
    content = output_path.read_text()
    
    assert "import bonsai.operators" in content
    assert "IfcWall" in content
    assert "create_wall('MainWall', (0, 0, 0), 5, 3)" in content
