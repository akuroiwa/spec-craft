import pytest
import json
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_read_storyboard_tool(temp_workspace):
    """Verify the read_storyboard tool returns structured data."""
    # Setup obsidian file
    obsidian_dir = temp_workspace / "obsidian"
    obsidian_dir.mkdir(parents=True, exist_ok=True)
    (obsidian_dir / "test.md").write_text("# Scene 1\nAction.")
    
    # Create server instance with the temp workspace
    mcp = create_mcp_server(temp_workspace)
    
    # FastMCP tool execution happens through call_tool (async)
    result = await mcp.call_tool("read_storyboard", {"path": "test.md"})
    
    # result is a ToolResult. We expect the data in the first content block.
    assert len(result.content) == 1
    # The content is usually a JSON string if the tool returns a dict
    data = json.loads(result.content[0].text)
    
    # Verify structure
    assert data["metadata"] == {}
    assert len(data["sections"]) == 1
    assert data["sections"][0]["title"] == "Scene 1"
    assert "Action." in data["sections"][0]["content"]

@pytest.mark.anyio
async def test_check_agent_extensions_tool(temp_workspace):
    """Verify the check_agent_extensions tool correctly reports status."""
    specify_dir = temp_workspace / ".specify"
    ext_file = specify_dir / "extensions.yml"
    ext_file.write_text("installed: [{extension: 'git'}]")
    
    mcp = create_mcp_server(temp_workspace)
    
    result = await mcp.call_tool("check_agent_extensions", {"required_extensions": ["git", "nano-banana"]})
    
    # result is a ToolResult
    data = json.loads(result.content[0].text)
    
    assert data[0]["name"] == "git"
    assert data[0]["is_installed"] is True
    
    assert data[1]["name"] == "nano-banana"
    assert data[1]["is_installed"] is False
    assert "gemini-cli extension install nano-banana" in data[1]["install_command"]
