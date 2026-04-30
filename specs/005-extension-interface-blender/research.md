# Research: Extension Interface & Blender Integration

## Decisions

### 1. spec-kit Extension Mechanism
- **Decision**: Use the `.specify/extensions/` local directory pattern to host the `spec-craft` extension manifest and command mappings.
- **Rationale**: This is the standard way to extend `spec-kit` without publishing to a central registry. It allows for immediate tactical integration.
- **Alternatives**: Publishing to a central registry (rejected as out of scope for development phase).

### 2. Blender Python API (bpy) Integration
- **Decision**: Provide a `blender_3d_guide` prompt that generates self-contained Python scripts using the `bpy` module.
- **Rationale**: `bpy` is the standard API for Blender automation. Generating standalone scripts allows users to run them via `blender --python script.py` or within the Blender text editor.
- **Alternatives**: Live socket connection to Blender (rejected due to complexity and environmental requirements).

### 3. "Bonkei" (Tray Landscape) Logic
- **Decision**: Define a specific set of geometric primitives and placement rules within the Blender prompt to simulate Bonkei construction (e.g., fractal landscapes, low-poly tree generation).
- **Rationale**: "Bonkei" is the chosen aesthetic for 3D scenes. Providing specific logic for this ensures visual consistency.
- **Alternatives**: General-purpose 3D guidance (rejected as too broad).

## Best Practices
- **Extension Naming**: Prefix all spec-craft commands with `obsidian-` to avoid name collisions with core spec-kit commands.
- **Blender Scripting**: Always include `import bpy` and `import bmesh` in generated scripts. Use modular functions for scene construction.
- **Full Pipeline Verification**: The integration test should use a dedicated "Gold Master" project that exercises SVG, CAD, and 3D paths.
