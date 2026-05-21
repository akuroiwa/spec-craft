# Tasks: Workflow Reliability Refinement

## Implementation Strategy
We will enhance the reliability of tactical task execution by removing problematic internal execution tools and replacing them with an AI-driven discovery model. We will first remove the `execute_tactical_script` tool from the MCP server. Then, we will add a bootstrapping prompt to guide the AI to read and follow the `spec-kit` TOML definitions. Finally, we will update the workspace analysis to provide the necessary metadata for this discovery.

## Phase 1: Setup
- [ ] T001 Remove `execute_tactical_script` tool from `src/spec_craft/mcp/server.py`

## Phase 2: Foundational
- [ ] T002 Define `BOOT_TACTICAL_KNOWLEDGE` constant in `src/spec_craft/mcp/prompts.py`
- [ ] T003 [P] Register `boot_tactical_knowledge` prompt in `src/spec_craft/mcp/server.py`

## Phase 3: User Story 1 - Secure Tactical Execution (Priority: P1)
**Goal**: Suggest commands to the user instead of hidden execution.
**Independent Test**: AI proposes a `bash` command instead of calling a hidden tool.

- [ ] T004 [US1] Update `src/spec_craft/mcp/prompts.py` to instruct AI to use `run_shell_command` for tactical scripts
- [ ] T005 [US1] Add a "Given/When/Then" scenario for tactical suggestions in `BOOT_TACTICAL_KNOWLEDGE`

## Phase 4: User Story 2 - Automated Tactical Knowledge (Priority: P2)
**Goal**: Automatically discover TOML definitions.
**Independent Test**: AI reads `.gemini/commands/` after calling `analyze_workspace`.

- [ ] T006 [US2] Update `WorkspaceDetector.get_metadata` in `src/spec_craft/core/detector.py` to include `agent_command_path`
- [ ] T007 [US2] Register updated `analyze_workspace` tool in `src/spec_craft/mcp/server.py`

## Phase 5: Polish
- [ ] T008 Update `README.md` to mention the new transparent tactical workflow
- [ ] T009 Final verification of SC-001 to SC-003 in Phase 13 spec

## Dependencies
- US1 (Execution) depends on tool removal (Phase 1).
- US2 (Discovery) depends on metadata updates (Phase 4).

## Parallel Execution Examples
- T003 (Registration) and T006 (Metadata) can be worked on in parallel.
