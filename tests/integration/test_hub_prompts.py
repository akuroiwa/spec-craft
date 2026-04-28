import pytest
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_mcp_prompts_registration():
    """Verify that all domain-specific prompts are registered and return content."""
    mcp = create_mcp_server()
    
    # Check registration
    prompts = await mcp.list_prompts()
    prompt_names = [p.name for p in prompts]
    
    assert "sdd_strategy_tactics" in prompt_names
    assert "manga_storyboard_guide" in prompt_names
    assert "video_production_guide" in prompt_names
    assert "cad_design_guide" in prompt_names
    
    # Check content of one prompt
    result = await mcp.render_prompt("sdd_strategy_tactics", arguments={})
    
    # result.messages[0].content is a TextContent (or similar)
    assert "Strategy (Obsidian)" in result.messages[0].content.text

@pytest.mark.anyio
async def test_bootstrap_constitution_prompt():
    """Verify that bootstrap_constitution prompt returns the SDD rules."""
    mcp = create_mcp_server()
    result = await mcp.render_prompt("bootstrap_constitution", arguments={})
    
    text = result.messages[0].content.text
    assert "### VI. Feature Branch Lifecycle" in text
    assert "### VIII. Git Commit Procedure" in text

@pytest.mark.anyio
async def test_agent_extension_guide_prompt():
    """Verify that agent_extension_guide prompt returns the directory mapping."""
    mcp = create_mcp_server()
    result = await mcp.render_prompt("agent_extension_guide", arguments={})
    
    text = result.messages[0].content.text
    assert "**Claude Code**" in text
    assert "`.claude/commands/`" in text
