# Implementation Plan: Final Refinement of JSCAD/Bonsai Drivers and Release Preparation

**Branch**: `011-refine-jscad-bonsai` | **Date**: 2026-04-25 | **Spec**: [specs/011-refine-release/spec.md](spec.md)
**Input**: Feature specification from `/specs/011-refine-release/spec.md`

## Summary
Refine the multi-domain drivers (JSCAD and Bonsai) to ensure production-quality asset generation. Finalize the Japanese documentation and establish a secure staging pipeline to Test PyPI. This phase prepares Spec-Craft for its first public release by resolving technical debt identified during verification.

## Technical Context

**Language/Version**: Python 3.10+, Node.js (npx), Blender 4.x  
**Primary Dependencies**: `fastmcp`, `sphinx-intl`, `twine` (for staging)  
**Storage**: Filesystem (`build/`, `docs/source/locale/`)  
**Testing**: `pytest` for driver logic and environment check.  
**Target Platform**: Linux / PyPI (Test)  
**Project Type**: Production Refinement / Release Staging  
**Performance Goals**: 100% test coverage for critical driver paths.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK.
- **IV. Cross-Domain Generative SDD**: OK. Refines CAD and BIM drivers.
- **VI. Feature Branch Lifecycle & Merging**: OK. All previous branches merged.
- **VII. In-Code Prompt Definition**: OK. All refined prompts remain in-code.

## Project Structure

### Documentation (this feature)

```text
specs/011-refine-release/
├── plan.md              # This file
├── research.md          # JSCAD CLI and Bonsai API research
├── data-model.md        # CADResult and Staging entities
├── quickstart.md        # Staging release guide
├── contracts/
│   └── refined_build.md # Driver and Detection contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   ├── detector.py  # Enhanced environment check
    │   └── drivers/
    │       ├── cad.py    # Refined (STL+SVG)
    │       └── bonsai.py # Refined (Bonsai API)
    └── mcp/
        ├── prompts.py   # Refined CAD/BIM guides
        └── server.py    # Updated tool registrations
docs/
└── source/
    └── locale/          # Completed JA translations
```

**Structure Decision**: Option 1 (Single project) focusing on driver logic and documentation.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
