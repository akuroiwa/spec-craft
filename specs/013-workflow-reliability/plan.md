# Implementation Plan: Workflow Reliability Refinement

**Branch**: `013-workflow-reliability` | **Date**: 2026-05-12 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/014-workflow-reliability/spec.md`

## Summary
Resolve reliability issues with tactical task execution by shifting from hidden internal execution to a transparent, AI-driven discovery model. This involves removing the problematic `execute_tactical_script` tool and replacing it with a bootstrapping prompt that allows the AI to read and follow the `spec-kit` TOML definitions for any given agent.

## Technical Context

**Language/Version**: Python 3.10+, spec-kit 0.8.x
**Primary Dependencies**: `fastmcp`, `spec-kit`
**Project Type**: Reliability / Architectural Refinement
**Performance Goals**: AI discovery of tactical knowledge < 1s.

## Constitution Check

- **II. Integrated SDD Lifecycle**: OK. Improving the robustness of the lifecycle.
- **VII. In-Code Prompt Definition**: OK. Adding the bootstrapping logic as an in-code prompt.
- **Git Commit Procedure**: OK. Manual execution will follow the constitution.

## Project Structure

### Documentation (this feature)

```text
specs/014-workflow-reliability/
├── plan.md              # This file
├── research.md          # Removal of internal tools research
├── data-model.md        # Tactical knowledge entities
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   └── detector.py  # Update analyze_workspace
    └── mcp/
        ├── prompts.py   # Add boot_tactical_knowledge
        └── server.py    # Remove execute_tactical_script
```

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
