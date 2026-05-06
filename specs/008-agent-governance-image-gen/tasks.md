# Tasks: Agent Governance and Image Generation Workflow

## Implementation Strategy
We will implement advanced agent governance and generative workflows by establishing a capability detection system and updating the guidance prompts. We will first implement the `CapabilityChecker` in the core logic, then update the MCP server to expose this through a new tool. Finally, we will define and register the generative workflow and updated extension guide prompts to bridge strategic roadmaps with tactical asset generation.

## Phase 1: Setup
- [X] T001 Define `GenerativeCapability` Pydantic model in `src/spec_craft/core/agent.py`

## Phase 2: Foundational
- [X] T002 [P] Implement `CapabilityChecker` class in `src/spec_craft/core/agent.py` to scan installed extensions and internal tools
- [X] T003 Define `AGENT_REGISTRY_URL` constant in `src/spec_craft/mcp/prompts.py`

## Phase 3: User Story 1 - Advanced Extension Discovery (Priority: P1)
**Goal**: Guide users to the official extension directory and provide tailored installation paths.
**Independent Test**: Render `agent_extension_guide` and verify it contains the `geminicli.com` link.

- [X] T004 [US1] Update `AGENT_EXTENSION_GUIDE_TEMPLATE` in `src/spec_craft/mcp/prompts.py` with registry URL and search tips
- [X] T005 [US1] Refine `agent_extension_guide` prompt in `src/spec_craft/mcp/server.py` to include agent-specific installation examples

## Phase 4: User Story 2 - Generative Workflow Integration (Priority: P2)
**Goal**: Establish a formalized "Generative Workflow" in MCP prompts.
**Independent Test**: Render `generative_workflow_guide` and verify the Strategic -> Tactics -> Implementation steps.

- [X] T006 [US2] Define `GENERATIVE_WORKFLOW_GUIDE` constant in `src/spec_craft/mcp/prompts.py`
- [X] T007 [US2] Register `generative_workflow_guide` prompt in `src/spec_craft/mcp/server.py`
- [X] T008 [US2] Add integration test for the generative build flow in `tests/integration/test_generative_flow.py`

## Phase 5: User Story 3 - Proactive Capability Detection (Priority: P3)
**Goal**: Proactively check for required generative tools before starting a creative task.
**Independent Test**: Call `check_generative_capabilities` for a missing domain and verify it returns correct install commands.

- [X] T009 [US3] Implement `check_generative_capabilities` logic in `AgentManager` within `src/spec_craft/core/agent.py`
- [X] T010 [US3] Register `check_generative_capabilities` tool in `src/spec_craft/mcp/server.py`
- [X] T011 [US3] Add unit tests for `CapabilityChecker` in `tests/unit/test_agent_capabilities.py`

## Phase 6: Polish
- [X] T012 Final verification of all success criteria (SC-001 to SC-004) in Phase 8 spec
- [X] T013 Update root `README.md` with mention of official extension registry

## Dependencies
- US3 (Detection) depends on T002 (CapabilityChecker).
- All prompt updates depend on the constants defined in Phase 2.

## Parallel Execution Examples
- T004 and T006 (Prompt strings) can be worked on in parallel.
- T011 (Unit tests) can be started once T002 is ready.
