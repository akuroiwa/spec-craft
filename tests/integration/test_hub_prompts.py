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
