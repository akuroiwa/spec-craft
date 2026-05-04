# Domain Guides

Spec-Craft supports multiple creative production domains.

## Manga Production
Define your storyboard in Obsidian. Use the `trigger_svg_build` tool to inject dialogue from your strategy into SVG templates.
- **Strategy**: YAML metadata in Obsidian.
- **Tactics**: Translated SVGs in the `build/` directory.

## CAD Modeling (JSCAD)
Specify geometric requirements in Obsidian. Use `trigger_cad_build` to generate JSCAD code and export STL files.
- **Visual Feedback**: AI can analyze generated SVGs to "see" the model's dimensions.

## 3D Scene Construction (Blender)
Describe tray landscapes (Bonkei) in Obsidian. Use `generate_blender_script` to create Python scripts for Blender.
- **Process**: Obsidian Spec → Blender Python Script → Automated 3D Build.
