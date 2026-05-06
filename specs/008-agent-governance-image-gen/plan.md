# Implementation Plan: Agent Governance and Image Generation Workflow

**Branch**: `008-phase-8-agent` | **Date**: 2026-04-25 | **Spec**: [specs/008-agent-governance-image-gen/spec.md](spec.md)
**Input**: Feature specification from `/specs/008-agent-governance-image-gen/spec.md`

## Summary
Implement advanced agent governance features, including proactive capability detection and an updated extension guide linked to the official registry. Establish a formalized "Generative Workflow" in MCP prompts to bridge Obsidian strategies with asset-generating extensions (like Nano Banana).

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: `fastmcp`, `pydantic`, `PyYAML`  
**Storage**: Filesystem (Markdown files and .specify config)  
**Testing**: `pytest` for capability detection logic.  
**Target Platform**: Linux / AI Agents (Gemini, Claude, Copilot)  
**Project Type**: MCP Server Enhancement  
**Performance Goals**: Capability check < 1s.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development with Obsidian**: OK. Directly connects creative strategies to implementations.
- **VII. In-Code Prompt Definition**: OK. New guides and workflows will be defined in-code.

## Project Structure

### Documentation (this feature)

```text
specs/008-agent-governance-image-gen/
├── plan.md              # This file
├── research.md          # Extension registry and detection research
├── data-model.md        # Capability and Registry entities
├── quickstart.md        # Governance and workflow examples
├── contracts/
│   └── mcp_agent.md     # Updated MCP contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
└── spec_craft/
    ├── core/
    │   └── agent.py     # Updated AgentManager with CapabilityChecker
    └── mcp/
        ├── prompts.py   # Updated guides and new generative workflows
        └── server.py    # Registered check_generative_capabilities tool
```

**Structure Decision**: Option 1 (Single project) remains standard.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
