import pytest
import json
from unittest.mock import patch, MagicMock
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_cad_visual_feedback_loop(temp_workspace):
    """Verify that trigger_cad_build handles multiple formats and returns paths."""
    mcp = create_mcp_server(temp_workspace)
    
    jscad_code = "cube();"
    
    # Mock subprocess.run to simulate successful npx execution
    # and manually create the files it would have created.
    def mock_run_side_effect(command, **kwargs):
        # command looks like ['npx', '@jscad/cli', '...', '--output', '...']
        out_path = command[4]
        from pathlib import Path
        Path(out_path).write_text("mock content")
        return MagicMock(returncode=0)

    with patch("subprocess.run", side_effect=mock_run_side_effect) as mock_run:
        result = await mcp.call_tool("trigger_cad_build", {
            "jscad_code": jscad_code,
            "output_name": "visual_part",
            "formats": ["stl", "svg"]
        })
        
        # result is a ToolResult
        data = json.loads(result.content[0].text)
        
        assert "stl" in data
        assert "svg" in data
        assert "build/cad/universal/visual_part.stl" in data["stl"]
        assert "build/cad/universal/visual_part.svg" in data["svg"]
        
        # Verify files exist in temp workspace
        assert (temp_workspace / data["stl"]).is_file()
        assert (temp_workspace / data["svg"]).is_file()
