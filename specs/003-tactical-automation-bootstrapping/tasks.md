# Tasks: Tactical Automation and Constitutional Bootstrapping

## Implementation Strategy
We will implement the tactical automation and bootstrapping features by first creating a robust script executor, then defining the portable SDD rules and agent profiles in-code, and finally exposing them via the FastMCP server. Security and path validation are critical for the script execution tool.

## Phase 1: Setup
- [X] T001 Create `src/spec_craft/core/executor.py` for tactical execution logic

## Phase 2: Foundational
- [X] T002 Implement `ScriptExecutor` class with safe subprocess handling in `src/spec_craft/core/executor.py`

## Phase 3: User Story 1 - Tactical Execution (Priority: P1)
**Goal**: AI can execute spec-kit tactical commands directly via MCP tools.
**Independent Test**: Use `execute_tactical_script` with `check-prerequisites.sh` and verify the captured output.

- [X] T003 [P] [US1] Create unit tests for `ScriptExecutor` in `tests/unit/test_executor.py`
- [X] T004 [US1] Register `execute_tactical_script` tool in `src/spec_craft/mcp/server.py`
- [X] T005 [US1] Add integration test for tactical script execution in `tests/integration/test_tactical_tools.py`

## Phase 4: User Story 2 - Constitutional Bootstrap (Priority: P2)
**Goal**: AI can automatically apply established SDD best practices to new project constitutions.
**Independent Test**: Render the `bootstrap_constitution` prompt and verify it contains Section VI, VII, and commit rules.

- [X] T006 [US2] Define `BOOTSTRAP_RULES` and `GIT_COMMIT_PROCEDURE` constants in `src/spec_craft/mcp/prompts.py`
- [X] T007 [US2] Register `bootstrap_constitution` prompt in `src/spec_craft/mcp/server.py`
- [X] T008 [US2] Add integration test for bootstrapping prompt in `tests/integration/test_tactical_prompts.py`

## Phase 5: User Story 3 - Agent Extension Discovery (Priority: P3)
**Goal**: AI guides users to correct extension installation paths for different agents.
**Independent Test**: Render `agent_extension_guide` for "Claude Code" and verify it mentions `.claude/commands/`.

- [X] T009 [US3] Define `AGENT_PROFILES` and mapping logic in `src/spec_craft/mcp/prompts.py`
- [X] T010 [US3] Register `agent_extension_guide` prompt in `src/spec_craft/mcp/server.py`
- [X] T011 [US3] Add integration test for extension guide prompt in `tests/integration/test_tactical_prompts.py`

## Phase 6: Polish
- [X] T012 Ensure all new automation tools have strict path validation to prevent execution outside `.specify/scripts/bash/`
- [X] T013 Final verification of all success criteria in `specs/003-tactical-automation-bootstrapping/spec.md`

## Dependencies
- US1 (Tactical Execution) depends on T002 (Executor).
- US2 and US3 depend on prompts registration in US1's phase.

## Parallel Execution Examples
- T003 (Executor tests) can be done in parallel with prompt definitions (T006, T009).
