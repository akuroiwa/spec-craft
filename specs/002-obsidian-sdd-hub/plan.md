# Implementation Plan: Obsidian-Driven SDD Hub - Storyboard Integration and Agent Management

**Branch**: `002-obsidian-hub-storyboard` | **Date**: 2026-04-25 | **Spec**: [specs/002-obsidian-sdd-hub/spec.md](spec.md)
**Input**: Feature specification from `/specs/002-obsidian-sdd-hub/spec.md`

## Summary
Implement the "Strategic Hub" functionality by adding an Obsidian storyboard parser and domain-specific MCP prompts. The foundation provides tools to analyze creative strategies and ensure the agent environment has the necessary capabilities (extensions) for implementation.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: `fastmcp`, `pydantic`, `PyYAML`, `gitpython`  
**Storage**: Filesystem (Obsidian Markdown files)  
**Testing**: `pytest`  
**Target Platform**: Linux  
**Project Type**: CLI / MCP Server  
**Performance Goals**: Storyboard parsing < 2s  
**Constraints**: In-code prompt definitions (no external .txt files for prompts)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Directly implements strategic analysis from Obsidian.
- **II. Integrated SDD Lifecycle**: OK. Following `spec-kit` workflow.
- **VII. In-Code Prompt Definition**: OK. Prompts will be bundled in `src/spec_craft/mcp/prompts.py`.

## Project Structure

### Documentation (this feature)

```text
specs/002-obsidian-sdd-hub/
├── plan.md              # This file
├── research.md          # YAML parsing and extension detection research
├── data-model.md        # Storyboard, Section, and ExtensionInfo entities
├── quickstart.md        # Usage examples for storyboards and prompts
├── contracts/
│   └── mcp_hub.md       # MCP tool and prompt contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   ├── parser.py    # StoryboardParser (Markdown + YAML)
    │   └── agent.py     # AgentManager (Extension detection)
    └── mcp/
        ├── prompts.py   # In-code prompt definitions (Manga, CAD, etc.)
        └── server.py    # Registered new tools and prompts
```

**Structure Decision**: Option 1 (Single project) remains the best fit.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
