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
- **Visual Verification**: Use `render_blender_svg` to generate line-art projections for AI analysis.

## Architectural Design (Bonsai)
Manage architectural strategies and tactical implementations using the IFC (Industry Foundation Classes) standard. Spec-Craft generates Python scripts that utilize the Bonsai (BlenderBIM) API to create BIM-compliant models.
- **Standards**: OpenBIM / IFC compliance.
- **Workflow**: Obsidian Strategy → Bonsai Python Script → IFC Asset Generation.
- **AI Verification**: AI can visually inspect walls and slabs using SVG projections to ensure compliance with the strategy.

## AI-Assisted Implementation (Emacs Sandbox)
Spec-Craft provides a dedicated Emacs sandbox to help AI agents write and verify code.
- **Isolation**: Uses a project-specific init directory (`.spec-craft/emacs/`) to avoid affecting your personal config.
- **Capabilities**: Pre-configured with LSP (Eglot), Linting (Flymake), and Tree-sitter for high-precision editing.
- **Workflow**: AI initializes the sandbox with `setup_emacs_sandbox` and performs edits via `edit_with_emacs`.
