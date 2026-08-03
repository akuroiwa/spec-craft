# Implementation Plan: Emacs Inspect and Parser Fix

**Branch**: `014-emacs-inspect-and` | **Date**: 2026-07-31 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/014-emacs-inspect-and/spec.md`

## Summary

Improve the Spec-Craft Emacs sandbox and StoryboardParser reliability:
1. Implement `eval_in_buffer()` in `EmacsManager` to query LSP/Flymake without modifying files on disk.
2. Replace static `time.sleep(1)` with loop polling during Emacs daemon startup to avoid race conditions.
3. Configure `global-auto-revert-mode` in the sandboxed Emacs instance.
4. Update `StoryboardParser` to ignore headings inside fenced code blocks.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: fastmcp, pydantic, PyYAML, lxml

**Storage**: Local files

**Testing**: pytest

**Target Platform**: Linux (Standard Ubuntu/Debian environment with Emacs 29.1+)

**Project Type**: Python CLI / MCP Server

**Performance Goals**: Emacs daemon startup completes within 30s.

**Constraints**: Sandbox isolation must be preserved (`.spec-craft/emacs/`).

**Scale/Scope**: Modified files:
- `src/spec_craft/core/emacs.py`
- `src/spec_craft/core/parser.py`
- `src/spec_craft/data/emacs/init.el`

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-Driven Development**: Specification and Plan directories are correctly generated under `specs/014-emacs-inspect-and/`.
- **uv Integration**: All tests and execution will be run via `uv run`.
- **Feature Branch Lifecycle**: Operating on branch `014-emacs-inspect-and`.
- **In-Code Prompts**: No prompts need modifications for this feature, but Emacs interaction matches existing rules.

---

## Project Structure

### Documentation (this feature)

```text
specs/014-emacs-inspect-and/
├── plan.md              # This file
├── research.md          # Research decisions
├── data-model.md        # Classes and data models definition
├── quickstart.md        # Quickstart and verification instructions
└── tasks.md             # Tasks to be created in the next phase
```

### Source Code

```text
src/
└── spec_craft/
    ├── core/
    │   ├── emacs.py     # Modify: Add eval_in_buffer, update start_daemon polling
    │   └── parser.py    # Modify: StoryboardParser code block tracking
    └── data/
        └── emacs/
            └── init.el  # Modify: Add global-auto-revert-mode
tests/
└── unit/
    ├── test_emacs.py    # Modify/Add tests for eval_in_buffer and daemon polling
    └── test_parser.py   # Modify/Add tests for code block comment ignore
```

**Structure Decision**: Single python project structure.

---

## Complexity Tracking

No violations of the project constitution.
