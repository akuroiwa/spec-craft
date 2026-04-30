import pytest
import json
from pathlib import Path
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_trigger_svg_build_cycle(temp_workspace):
    """Verify the full SVG build cycle: Obsidian spec -> Template -> Build output."""
    # 1. Setup Obsidian dictionary
    obsidian_dir = temp_workspace / "obsidian" / "ja"
    obsidian_dir.mkdir(parents=True, exist_ok=True)
    (obsidian_dir / "scene1.md").write_text("""---
translations:
  greeting: "こんにちは"
---
# Scene 1 Strategy
""")

    # 2. Setup SVG template
    template_dir = temp_workspace / "templates"
    template_dir.mkdir(parents=True, exist_ok=True)
    (template_dir / "comic.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><text id="greeting">Hello</text></svg>')

    # 3. Trigger build via MCP tool
    mcp = create_mcp_server(temp_workspace)
    result_path_str = await mcp.call_tool("trigger_svg_build", {
        "template_path": "comic.svg",
        "obsidian_path": "ja/scene1.md",
        "lang": "ja"
    })
    
    # result_path_str is a ToolResult
    result_path = result_path_str.content[0].text.strip('"')
    
    # 4. Verify output
    full_output_path = temp_workspace / result_path
    assert full_output_path.is_file()
    assert "build/manga/ja/comic.svg" in str(result_path)
    
    content = full_output_path.read_text()
    assert "こんにちは" in content

@pytest.mark.anyio
async def test_trigger_cad_build_cycle(temp_workspace):
    """Verify the CAD build cycle: Code -> STL generation."""
    # Setup: Create a mock jscad-tool.js that actually touches the output file
    mock_tool = """
import fs from 'fs';
const outPath = process.argv[4]; // -o <path>
fs.writeFileSync(outPath, 'mock stl content');
console.log('Mock Success');
"""
    (temp_workspace / "jscad-tool.js").write_text(mock_tool)
    
    mcp = create_mcp_server(temp_workspace)
    
    jscad_code = "function main() { return cube(); }"
    result_path_str = await mcp.call_tool("trigger_cad_build", {
        "jscad_code": jscad_code,
        "output_name": "part.stl"
    })
    
    # result_path_str is a ToolResult
    result_path = result_path_str.content[0].text.strip('"')
    
    # Verify output files
    assert "build/cad/universal/part.stl" in result_path
    assert (temp_workspace / result_path).is_file()
    assert (temp_workspace / result_path).with_suffix(".js").is_file()
