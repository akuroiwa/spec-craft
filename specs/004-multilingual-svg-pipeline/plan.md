# Implementation Plan: Multilingual SVG Pipeline and Multi-domain Build Integration

**Branch**: `004-multilingual-svg-pipeline` | **Date**: 2026-04-25 | **Spec**: [specs/004-multilingual-svg-pipeline/spec.md](spec.md)
**Input**: Feature specification from `/specs/004-multilingual-svg-pipeline/spec.md`

## Summary
Implement the generation pipeline for assets (SVG, STL) with multi-language support. This involves creating drivers for SVG manipulation (text injection) and CAD generation (JSCAD), coordinated by a centralized BuildManager that organizes output into hierarchical directories.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: `fastmcp`, `pydantic`, `lxml`, `PyYAML`, `gitpython`  
**External Tools**: `node`, `jscad-tool.js`  
**Storage**: Filesystem (`obsidian/`, `build/`, `templates/`)  
**Testing**: `pytest`  
**Target Platform**: Linux  
**Project Type**: Generation Pipeline / MCP Server  
**Performance Goals**: SVG text replacement < 500ms.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK.
- **IV. Cross-Domain Generative SDD**: OK. Implements 2D (SVG) and 3D (CAD) production.
- **V. Package Management with uv**: OK.
- **VII. In-Code Prompt Definition**: OK.

## Project Structure

### Documentation (this feature)

```text
specs/004-multilingual-svg-pipeline/
├── plan.md              # This file
├── research.md          # SVG and CAD integration research
├── data-model.md        # Asset, Template, and Dictionary entities
├── quickstart.md        # Usage examples for asset generation
├── contracts/
│   └── mcp_build.md     # MCP build tools and prompt contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   ├── build.py     # BuildManager (Directory coordination)
    │   └── drivers/
    │       ├── svg.py   # SVGDriver (lxml based injection)
    │       └── cad.py   # CADDriver (JSCAD subprocess wrapper)
    └── mcp/
        └── server.py    # Registered trigger_svg_build and trigger_cad_build tools
```

**Structure Decision**: Option 1 (Single project) with a `drivers/` sub-package for domain-specific generation logic.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
