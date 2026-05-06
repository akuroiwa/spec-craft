import yaml
import pytest
from pathlib import Path
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_extension_manifest_consistency():
    """Verify extension.yml commands map to existing MCP tools."""
    from importlib import resources
    p_ext = resources.files("spec_craft.data").joinpath("extension")
    manifest_path = p_ext.joinpath("extension.yml")
    
    assert manifest_path.is_file()
    
    with manifest_path.open("r") as f:
        manifest = yaml.safe_load(f)
    
    mcp = create_mcp_server()
    tools = await mcp.list_tools()
    registered_tools = [tool.name for tool in tools]
    
    for cmd in manifest.get("commands", []):
        tool_name = cmd.get("mcp_tool")
        assert tool_name in registered_tools, f"Command {cmd['name']} maps to missing tool {tool_name}"
