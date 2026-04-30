import pytest
import json
from pathlib import Path
from spec_craft.mcp.server import create_mcp_server

@pytest.mark.anyio
async def test_full_gold_master_pipeline(temp_workspace):
    """Verify all asset domains (Manga, CAD, 3D) are operational in one project."""
    
    # 1. Setup Project Structure
    (temp_workspace / "templates").mkdir()
    (temp_workspace / "obsidian" / "en").mkdir(parents=True)
    # Correct mock for JSCAD tool
    mock_tool = """
const fs = require('fs');
fs.writeFileSync(process.argv[4], 'stl');
"""
    (temp_workspace / "jscad-tool.js").write_text(mock_tool)
    (temp_workspace / "templates" / "main.svg").write_text('<svg id="title">Title</svg>')
    (temp_workspace / "obsidian" / "en" / "spec.md").write_text("---\ntranslations: {title: 'Master'}\n---\n")

    mcp = create_mcp_server(temp_workspace)

    # 2. Trigger Manga (SVG)
    res_svg = await mcp.call_tool("trigger_svg_build", {
        "template_path": "main.svg", "obsidian_path": "en/spec.md", "lang": "en"
    })
    
    # 3. Trigger CAD (STL)
    res_cad = await mcp.call_tool("trigger_cad_build", {
        "jscad_code": "cube()", "output_name": "base.stl"
    })
    
    # 4. Trigger 3D (Blender)
    res_3d = await mcp.call_tool("generate_blender_script", {
        "scene_spec": {"width": 10}, "output_name": "scene.py"
    })

    # 5. Verify Artifacts
    svg_path = temp_workspace / res_svg.content[0].text.strip('"')
    stl_path = temp_workspace / res_cad.content[0].text.strip('"')
    py_path = temp_workspace / res_3d.content[0].text.strip('"')

    assert svg_path.is_file() and "Master" in svg_path.read_text()
    assert stl_path.is_file()
    assert py_path.is_file() and "import bpy" in py_path.read_text()

    # 6. Check Directory Organization
    assert "build/manga/en/" in str(svg_path)
    assert "build/cad/universal/" in str(stl_path)
    assert "build/3d/universal/" in str(py_path)
