# Implementation Plan: spec-kit Extension Interface and 3D Integration via Blender

**Branch**: `005-extension-interface-blender` | **Date**: 2026-04-25 | **Spec**: [specs/005-extension-interface-blender/spec.md](spec.md)
**Input**: Feature specification from `/specs/005-extension-interface-blender/spec.md`

## Summary
Implement the final integration layer by providing a spec-kit extension interface and specialized prompts for 3D scene generation in Blender. This phase connects tactical slash commands to the Obsidian Strategic Hub and expands creative output to the 3D domain (Bonkei logic).

## Technical Context

**Language/Version**: Python 3.10+, Blender 4.x (bpy)  
**Primary Dependencies**: `fastmcp`, `pydantic`, `PyYAML`, `gitpython`  
**Storage**: Filesystem (`.specify/extensions/`, `build/3d/`)  
**Testing**: `pytest`  
**Target Platform**: Linux  
**Project Type**: spec-kit Extension / 3D Asset Pipeline  
**Performance Goals**: Pipeline integration test < 15s.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK.
- **II. Integrated SDD Lifecycle**: OK. Directly extends the spec-kit workflow.
- **IV. Cross-Domain Generative SDD**: OK. Adds 3D (Blender) support.
- **VII. In-Code Prompt Definition**: OK.

## Project Structure

### Documentation (this feature)

```text
specs/005-extension-interface-blender/
├── plan.md              # This file
├── research.md          # Extension and Blender API research
├── data-model.md        # Extension and Bonkei entities
├── quickstart.md        # Extension setup and Blender usage
├── contracts/
│   └── extension_3d.md  # spec-kit command and Blender contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   └── drivers/
    │       └── blender.py # BlenderDriver (Script generation)
    └── mcp/
        ├── prompts.py     # blender-3d-guide prompt
        └── server.py      # Registered generate_blender_script tool
extension/                 # Local spec-kit extension folder
└── extension.yml          # Command mapping manifest
```

**Structure Decision**: Option 1 (Single project) with an added `extension/` directory for the spec-kit manifest.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
