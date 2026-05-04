# Implementation Plan: Multilingual Documentation with Sphinx and gettext

**Branch**: `006-multilingual-docs-sphinx` | **Date**: 2026-04-25 | **Spec**: [specs/006-multilingual-docs-sphinx/spec.md](spec.md)
**Input**: Feature specification from `/specs/006-multilingual-docs-sphinx/spec.md`

## Summary
Implement a multi-language documentation system using Sphinx and the gettext workflow. This involves setting up the environment, writing the core manual in English Markdown (via MyST), and establishing the pipeline for Japanese translation via PO files.

## Technical Context

**Language/Version**: Python 3.10+, Sphinx 7.x  
**Primary Dependencies**: `uv`, `sphinx`, `sphinx-intl`, `myst-parser`, `sphinx_rtd_theme`  
**Storage**: Filesystem (`docs/source/`, `docs/source/locale/`)  
**Testing**: HTML link checking and PO file validation  
**Target Platform**: Web Browser (HTML output)  
**Project Type**: Documentation / Localization  
**Performance Goals**: Full rebuild (EN+JA) < 20s.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Manual will explain the Strategy/Tactics relationship.
- **V. Package Management with uv**: OK. Sphinx and its extensions will be added as dev dependencies via `uv`.

## Project Structure

### Documentation (this feature)

```text
specs/006-multilingual-docs-sphinx/
├── plan.md              # This file
├── research.md          # Sphinx and gettext decisions
├── data-model.md        # ManualSource, POT, and PO entities
├── quickstart.md        # Doc build workflow commands
├── contracts/
│   └── doc_build.md     # Makefile targets contract
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
docs/
├── Makefile             # Build automation
├── make.bat             # Windows build support
└── source/
    ├── conf.py          # Sphinx configuration
    ├── index.md         # Manual entry point
    ├── strategy.md      # Strategic Hub documentation
    ├── installation.md  # Setup guide
    ├── domain-guides.md # Domain-specific instructions
    └── locale/          # gettext translation storage (PO files)
```

**Structure Decision**: Option 1 (Single project) with a dedicated `docs/` folder.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
