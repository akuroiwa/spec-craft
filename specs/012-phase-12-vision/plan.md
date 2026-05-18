# Implementation Plan: Vision Feedback and Isolated Editing Environment

**Branch**: `012-phase-12-vision` | **Date**: 2026-05-12 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/012-phase-12-vision/spec.md`

## Summary
Expand the Spec-Craft generative pipeline with visual verification for 3D assets (Blender) and establish an isolated Emacs environment for high-precision AI editing. This phase focuses on closing the feedback loop between 3D script generation and visual intent, while providing the AI agent with a professional-grade editor sandbox.

## Technical Context

**Language/Version**: Python 3.10+, Emacs 29+, Blender 4.x
**Primary Dependencies**: `fastmcp`, `emacsclient`, `render_freestyle_svg`
**Storage**: Filesystem (`.spec-craft/emacs/`, `build/3d/`)
**Testing**: `pytest` for Emacs command execution and SVG generation verification.
**Target Platform**: Linux (Standard for daemon support)
**Project Type**: Generative SDD / AI-assisted Development
**Performance Goals**: Emacs edits < 2s, SVG rendering < 5s.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Vision feedback maps back to strategic intent.
- **IV. Cross-Domain Generative SDD**: OK. Extends 3D verification and code editing domains.
- **VII. In-Code Prompt Definition**: OK. All Emacs guides and rendering rules will be in-code.

## Project Structure

### Documentation (this feature)

```text
specs/012-phase-12-vision/
├── plan.md              # This file
├── research.md          # Freestyle SVG and Emacs isolation research
├── data-model.md        # Sandbox and Render entities
├── quickstart.md        # Vision and Sandbox usage
├── contracts/
│   └── mcp_vision_edit.md # Updated MCP tool definitions
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   ├── emacs.py      # New EmacsManager (daemon/sandbox)
    │   └── drivers/
    │       └── blender.py # Updated for Freestyle support
    └── mcp/
        └── server.py     # Registered render and sandbox tools
```

**Structure Decision**: Option 1 (Single project) remains standard.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| External Tool Dependency | Emacs/Blender for high-fidelity work | LLM internal generation lacks validation logic |
