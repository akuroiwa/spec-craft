# Implementation Plan: Tactical Automation and Constitutional Bootstrapping

**Branch**: `003-tactical-automation-bootstrapping` | **Date**: 2026-04-25 | **Spec**: [specs/003-tactical-automation-bootstrapping/spec.md](spec.md)
**Input**: Feature specification from `/specs/003-tactical-automation-bootstrapping/spec.md`

## Summary
Implement automated execution of spec-kit bash scripts via MCP and provide in-code prompts for bootstrapping project rules and discovering agent extension paths. This phase streamlines the tactical workflow and ensures high-quality SDD practices are easily adopted.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: `fastmcp`, `pydantic`, `subprocess` (built-in)  
**Storage**: Filesystem (Executing .sh files, reading .md files)  
**Testing**: `pytest`  
**Target Platform**: Linux  
**Project Type**: MCP Server / CLI Extension  
**Performance Goals**: Script execution < 3s for check commands.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Phase 3 facilitates the "Tactics" part of the SDD cycle.
- **II. Integrated SDD Lifecycle**: OK. Directly automates lifecycle steps.
- **VII. In-Code Prompt Definition**: OK. All bootstrap rules and guide metadata will be in-code.

## Project Structure

### Documentation (this feature)

```text
specs/003-tactical-automation-bootstrapping/
├── plan.md              # This file
├── research.md          # Subprocess and agent mapping research
├── data-model.md        # Script, Rule, and Profile entities
├── quickstart.md        # Automation and bootstrap examples
├── contracts/
│   └── mcp_tactics.md   # MCP automation tool and prompt contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   └── executor.py  # ScriptExecutor (Subprocess logic)
    └── mcp/
        ├── prompts.py   # Bootstrap rules and Agent metadata constants
        └── server.py    # Registered execute_tactical_script tool
```

**Structure Decision**: Option 1 (Single project) remains the standard.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
