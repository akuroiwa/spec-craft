import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from spec_craft.core.drivers.cad import CADDriver

def test_cad_driver_build_multi_format(temp_workspace):
    """Verify that CADDriver calls npx correctly for multiple formats."""
    driver = CADDriver(temp_workspace)
    
    jscad_code = "function main() { return cube(); }"
    output_base = temp_workspace / "build" / "cad" / "test"
    formats = ["stl", "svg"]
    
    # Mock subprocess.run and file existence
    with patch("subprocess.run") as mock_run, \
         patch("pathlib.Path.is_file") as mock_exists:
        mock_run.return_value = MagicMock(returncode=0, stdout="Success", stderr="")
        mock_exists.return_value = True

        results = driver.build(jscad_code, output_base, formats)
        assert len(results) == 2
        assert "stl" in results
        assert "svg" in results
        assert results["stl"] == output_base.with_suffix(".stl")
        assert results["svg"] == output_base.with_suffix(".svg")
        
        # Verify .js file was saved
        assert output_base.with_suffix(".js").is_file()
        assert output_base.with_suffix(".js").read_text() == jscad_code
        
        # Verify npx command was called twice
        assert mock_run.call_count == 2
        args1 = mock_run.call_args_list[0][0][0]
        assert "npx" in args1
        assert "@jscad/cli" in args1
