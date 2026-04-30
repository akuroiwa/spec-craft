# MCP & Extension Contract: Extension Interface & 3D Integration

## spec-kit Commands

### `/speckit.obsidian-analyze`
- **Purpose**: Analyze the current Obsidian storyboard and roadmap.
- **Maps to**: `read_storyboard` MCP tool.

### `/speckit.obsidian-build`
- **Purpose**: Trigger a full asset build (SVG, CAD, 3D).
- **Maps to**: `trigger_full_build` tool (TBD).

## MCP Tools

### `generate_blender_script`
- **Purpose**: Create a Python script for Blender scene construction.
- **Input**: `scene_spec` (JSON)
- **Output**: Content of the `.py` script.

## Prompts

### `blender-3d-guide`
- **Role**: Provides rules for low-poly scene construction and tray-landscape (Bonkei) logic using `bpy`.
