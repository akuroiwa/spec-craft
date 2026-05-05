# Implementation Plan: JSCAD Visual Feedback Loop and 3D Preview UI

**Branch**: `007-jscad-visual-feedback` | **Date**: 2026-04-25 | **Spec**: [specs/007-jscad-visual-feedback-ui/spec.md](spec.md)
**Input**: Feature specification from `/specs/007-jscad-visual-feedback-ui/spec.md`

## Summary
Normalize the JSCAD build process by replacing the mock driver with actual `npx @jscad/cli` calls to generate both STL and SVG artifacts. Implement a local Three.js-based previewer served via a custom Python web server, enabling immediate visual validation by both humans and AI agents.

## Technical Context

**Language/Version**: Python 3.10+, Node.js (npx)  
**Primary Dependencies**: `fastmcp`, `importlib.resources`, `http.server`, `Three.js` (bundled)  
**Storage**: Filesystem (`build/cad/`)  
**Testing**: `pytest` for server logic and driver output.  
**Target Platform**: Linux / Web Browser  
**Project Type**: CLI Extension / Multi-format Builder  
**Performance Goals**: CAD build < 5s, Preview startup < 2s.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Visual feedback cycle strengthens the SDD approach.
- **IV. Cross-Domain Generative SDD**: OK. Integrates advanced CAD validation.
- **VII. In-Code Prompt Definition**: OK. All preview-related prompts will be in-code.

## Project Structure

### Documentation (this feature)

```text
specs/007-jscad-visual-feedback-ui/
├── plan.md              # This file
├── research.md          # JSCAD CLI and Python server research
├── data-model.md        # CADResult and Server entities
├── quickstart.md        # Generation and preview guide
├── contracts/
│   └── interface.md     # CLI and MCP contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   ├── drivers/
    │   │   └── cad.py    # Updated CADDriver (npx based)
    │   └── ui/
    │       └── server.py # PreviewServer (http.server based)
    ├── static/           # Bundled web assets
    │   ├── index.html    # Three.js viewer
    │   └── viewer.js     # STL loading logic
    └── mcp/
        └── server.py     # Registered multi-format build tool
```

**Structure Decision**: Option 1 (Single project) with a new `static/` directory for web assets and a `ui/` module for the server.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
