# Quickstart: Phase 5 Features

## Installing the spec-kit Extension
1. Copy the `spec-craft` extension folder to `.specify/extensions/`.
2. The AI will now recognize `/speckit.obsidian-*` commands.

## Generating 3D Scenes
1. Define a "Bonkei" scene in your Obsidian storyboard.
2. Ask the AI: "Generate the Blender script for my tray landscape."
3. The AI will use the `blender-3d-guide` prompt to create `build/3d/bonkei.py`.

## Running the Blender Script
```bash
blender --python build/3d/bonkei.py
```
