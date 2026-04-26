# Tasks: Obsidian-Driven SDD Hub - Storyboard Integration and Agent Management

## Implementation Strategy
We will implement the Strategic Hub by first creating the core parsing and agent management logic, then defining the domain-specific prompts, and finally exposing everything through the FastMCP server. Verification will involve unit tests for the parser and integration tests for the MCP tools/prompts.

## Phase 1: Setup
- [X] T001 Update `pyproject.toml` to include `PyYAML` dependency in the root directory
- [X] T002 Sync dependencies using `uv sync` in the root directory
- [X] T003 Create `src/spec_craft/core/parser.py`, `src/spec_craft/core/agent.py`, and `src/spec_craft/mcp/prompts.py` files

## Phase 2: Foundational
- [X] T004 [P] Implement `StoryboardParser` with YAML and Markdown header support in `src/spec_craft/core/parser.py`
- [X] T005 [P] Implement `AgentManager` for extension detection in `src/spec_craft/core/agent.py`
- [X] T006 Update `README.md` to include the "Strategy vs Tactics" section in the root directory

## Phase 3: User Story 1 - Storyboard Evolution (Priority: P1)
**Goal**: AI can read and analyze Obsidian storyboards to understand strategy.
**Independent Test**: Use the `read_storyboard` tool with a sample file and verify the structured output.

- [X] T007 [P] [US1] Create unit tests for `StoryboardParser` in `tests/unit/test_parser.py`
- [X] T008 [US1] Register `read_storyboard` tool in `src/spec_craft/mcp/server.py`
- [X] T009 [US1] Add integration test for `read_storyboard` tool in `tests/integration/test_hub_tools.py`

## Phase 4: User Story 2 - Domain-Specific Guidance (Priority: P2)
**Goal**: Bundle domain knowledge (Manga, Video, CAD) as in-code FastMCP Prompts.
**Independent Test**: List MCP prompts and verify their content matches domain rules.

- [X] T010 [US2] Define `sdd-strategy-tactics` and `manga-storyboard-guide` prompts in `src/spec_craft/mcp/prompts.py`
- [X] T011 [US2] Define `video-production-guide` and `cad-design-guide` prompts in `src/spec_craft/mcp/prompts.py`
- [X] T012 [US2] Register all prompts in `src/spec_craft/mcp/server.py`
- [X] T013 [US2] Add integration test for MCP prompts in `tests/integration/test_hub_prompts.py`

## Phase 5: User Story 3 - Agent Capability Management (Priority: P3)
**Goal**: Detect missing agent extensions and suggest installation.
**Independent Test**: Use `check_agent_extensions` tool and verify it suggests correct installation commands.

- [X] T014 [P] [US3] Create unit tests for `AgentManager` in `tests/unit/test_agent.py`
- [X] T015 [US3] Register `check_agent_extensions` tool in `src/spec_craft/mcp/server.py`
- [X] T016 [US3] Add integration test for `check_agent_extensions` tool in `tests/integration/test_hub_tools.py`

## Phase 6: Polish
- [X] T017 Ensure all new tools and prompts have comprehensive docstrings and clear instructions
- [X] T018 Final verification of all SC-001 to SC-004 criteria in `specs/002-obsidian-sdd-hub/spec.md`

## Dependencies
- US1 (Storyboard Evolution) depends on T004 (Parser).
- US2 (Domain Guidance) depends on T003 (File creation).
- US3 (Agent Management) depends on T005 (Agent logic).

## Parallel Execution Examples
- T004, T005, T006 can be worked on in parallel once Phase 1 is complete.
- T007 (Parser tests) and T014 (Agent tests) can be worked on in parallel.
- T010 and T011 (Prompt definitions) can be worked on in parallel.
