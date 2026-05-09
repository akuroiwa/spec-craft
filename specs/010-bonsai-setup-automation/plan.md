# Implementation Plan: Bonsai (BlenderBIM) Integration and Setup Automation

**Branch**: `010-integrate-bonsai-blenderbim` | **Date**: 2026-04-25 | **Spec**: [specs/010-bonsai-setup-automation/spec.md](spec.md)
**Input**: Feature specification from `/specs/010-bonsai-setup-automation/spec.md`

## Summary
Implement professional architectural support via Bonsai (BlenderBIM) and provide proactive environment automation. This phase completes the creative toolset and prepares Spec-Craft for public staging on Test PyPI.

## Technical Context

**Language/Version**: Python 3.10+, Blender 4.x, Bonsai API  
**Primary Dependencies**: `fastmcp`, `importlib.util`, `shutil`  
**Storage**: Filesystem (`obsidian/`, `build/bonsai/`)  
**Testing**: `pytest` for environment detection logic.  
**Target Platform**: Linux / Windows / Web Browser  
**Project Type**: BIM Integration / Dev-Ops Toolkit  
**Performance Goals**: Environment check < 1s.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Architectural strategy is managed in Obsidian.
- **IV. Cross-Domain Generative SDD**: OK. Introduces professional BIM (Bonsai) support.
- **VII. In-Code Prompt Definition**: OK. All BIM guides and release checklists will be in-code.

## Project Structure

### Documentation (this feature)

```text
specs/010-bonsai-setup-automation/
├── plan.md              # This file
├── research.md          # Bonsai API and release research
├── data-model.md        # IFC Entity and Prerequisite entities
├── quickstart.md        # Environment and Bonsai guides
├── contracts/
│   └── mcp_bonsai.md    # Updated MCP contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   ├── detector.py  # Extended for environment check
    │   └── drivers/
    │       └── bonsai.py # BonsaiDriver (IFC Script generation)
    └── mcp/
        ├── prompts.py   # Bonsai guides and Test PyPI checklists
        └── server.py    # Registered check_environment tool
```

**Structure Decision**: Option 1 (Single project) remains standard.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
