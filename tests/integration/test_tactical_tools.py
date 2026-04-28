import pytest
import json
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_execute_tactical_script_tool(temp_workspace):
    """Verify the execute_tactical_script tool runs a script and returns output."""
    # Setup mock script
    scripts_dir = temp_workspace / ".specify" / "scripts" / "bash"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    (scripts_dir / "test.sh").write_text("#!/bin/bash\necho 'Success'")
    
    mcp = create_mcp_server(temp_workspace)
    
    result = await mcp.call_tool("execute_tactical_script", {"script_name": "test.sh"})
    
    # result is a ToolResult
    data = json.loads(result.content[0].text)
    
    assert data["exit_code"] == 0
    assert "Success" in data["stdout"]
