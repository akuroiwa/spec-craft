# Implementation Plan: Project Foundation - Initialize Python Package and MCP Server Base

**Branch**: `001-init-python-mcp-base` | **Date**: 2026-04-25 | **Spec**: [specs/001-project-foundation-init/spec.md](spec.md)
**Input**: Feature specification from `/specs/001-project-foundation-init/spec.md`

## Summary
Initialize a PEP 621 compliant Python package (`spec-craft`) with FastMCP and GitPython. The foundation provides a unified CLI entry point that can start an MCP server and detect workspace metadata (Git, Obsidian, Specify).

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: `fastmcp`, `pydantic`, `python-dotenv`, `gitpython`  
**Storage**: Filesystem (Markdown and YAML)  
**Testing**: `pytest`  
**Target Platform**: Linux  
**Project Type**: CLI / MCP Server / Library  
**Performance Goals**: CLI startup < 1s, Editable install < 30s  
**Constraints**: PEP 621 compliant, Multi-line commit safety via temporary files

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Foundation includes `WorkspaceDetector` for Obsidian folders.
- **II. Integrated SDD Lifecycle**: OK. Following `spec-kit` workflow.
- **III. Test-First Implementation**: OK. `pytest` selected for behavioral verification.
- **Git Commit Procedure**: OK. Instruction to use `.gemini/commit_msg.txt` is noted for the implementation phase.

## Project Structure

### Documentation (this feature)

```text
specs/001-project-foundation-init/
├── plan.md              # This file
├── research.md          # Research findings
├── data-model.md        # Workspace and Config entities
├── quickstart.md        # Setup and execution guide
├── contracts/
│   └── cli_mcp.md       # CLI and MCP tool contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
pyproject.toml           # PEP 621 package config
src/
└── spec_craft/
    ├── __init__.py
    ├── main.py          # CLI Entry point & MCP runner
    ├── core/
    │   ├── __init__.py
    │   ├── detector.py  # WorkspaceDetector
    │   └── manager.py   # ConstitutionManager base
    └── mcp/
        ├── __init__.py
        └── server.py    # FastMCP Server definition

tests/
├── conftest.py
├── integration/
└── unit/
```

**Structure Decision**: Single project (Option 1) is selected as this is a unified utility package.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
