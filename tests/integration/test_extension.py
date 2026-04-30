import yaml
import pytest
from pathlib import Path
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_extension_manifest_consistency():
    """Verify extension.yml commands map to existing MCP tools."""
    project_root = Path(__file__).parent.parent.parent
    manifest_path = project_root / "extension" / "extension.yml"
    
    assert manifest_path.is_file()
    
    with open(manifest_path, "r") as f:
        manifest = yaml.safe_load(f)
    
    mcp = create_mcp_server()
    tools = await mcp.list_tools()
    registered_tools = [tool.name for tool in tools]
    
    for cmd in manifest.get("commands", []):
        tool_name = cmd.get("mcp_tool")
        assert tool_name in registered_tools, f"Command {cmd['name']} maps to missing tool {tool_name}"
