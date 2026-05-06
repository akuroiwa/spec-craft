import pytest
import json
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_generative_workflow_integration(temp_workspace):
    """Verify the integration tool check_generative_capabilities works as expected."""
    mcp = create_mcp_server(temp_workspace)
    
    # 1. Check for missing manga capability
    result = await mcp.call_tool("check_generative_capabilities", {"domain": "manga"})
    data = json.loads(result.content[0].text)
    
    assert data["domain"] == "manga"
    assert data["is_ready"] is False
    assert "nano-banana" in data["required_extension"]

    # 2. Simulate installation
    specify_dir = temp_workspace / ".specify"
    specify_dir.mkdir(exist_ok=True)
    (specify_dir / "extensions.yml").write_text("installed: [{extension: 'nano-banana'}]")
    
    # 3. Check again
    result_ready = await mcp.call_tool("check_generative_capabilities", {"domain": "manga"})
    data_ready = json.loads(result_ready.content[0].text)
    
    assert data_ready["is_ready"] is True
