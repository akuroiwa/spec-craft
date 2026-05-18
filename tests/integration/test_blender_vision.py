import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from spec_craft.core.drivers.blender import BlenderDriver

def test_blender_driver_render_svg_mock(temp_workspace):
    """Verify that BlenderDriver calls blender headlessly."""
    driver = BlenderDriver(temp_workspace)
    script_path = temp_workspace / "build" / "3d" / "scene.py"
    output_svg = temp_workspace / "build" / "3d" / "render.svg"
    
    # Ensure script exists
    script_path.parent.mkdir(parents=True, exist_ok=True)
    script_path.touch()
    
    with patch("subprocess.run") as mock_run:
        # Simulate success
        mock_run.return_value = MagicMock(returncode=0)
        
        with patch.object(Path, "is_file", autospec=True) as mock_is_file:
            def side_effect(path_obj):
                if str(path_obj).endswith("render.svg"): return True
                if str(path_obj).endswith("scene.py"): return True
                return False
            mock_is_file.side_effect = side_effect
            
            result = driver.render_svg(script_path, output_svg)
            
            assert result == output_svg
            args, kwargs = mock_run.call_args
            command = args[0]
            assert "blender" in command
            assert "-b" in command
            assert "-P" in command
