# Tasks: Project Foundation - Initialize Python Package and MCP Server Base

## Implementation Strategy
We will follow an MVP-first approach, focusing on establishing the core package structure and a working MCP server. Verification will be performed incrementally using `pytest` and manual CLI tests.

## Phase 1: Setup
- [X] T001 Initialize `pyproject.toml` with PEP 621 metadata and dependencies in the root directory
- [X] T002 Create initial `README.md` with project description in the root directory
- [X] T003 Setup directory structure: `src/spec_craft/{core,mcp}` and `tests/{unit,integration}`

## Phase 2: Foundational
- [X] T004 Create `src/spec_craft/__init__.py` with package version
- [X] T005 [P] Create `tests/conftest.py` for shared pytest fixtures
- [X] T006 [P] Implement `src/spec_craft/core/detector.py` for workspace detection (Git, Obsidian, .specify)
- [X] T007 Implement `src/spec_craft/core/manager.py` base for Constitution management

## Phase 3: User Story 1 - Environment Setup (Priority: P1)
**Goal**: Initialize a standard Python package structure and MCP server base.
**Independent Test**: Run `pip install -e .` and `spec-craft serve` to verify server startup.

- [X] T008 [P] [US1] Create unit tests for `WorkspaceDetector` in `tests/unit/test_detector.py`
- [X] T009 [US1] Implement `src/spec_craft/mcp/server.py` with basic FastMCP server and `analyze_workspace` tool
- [X] T010 [US1] Implement `src/spec_craft/main.py` entry point with `serve` and `--version` subcommands
- [X] T011 [US1] Verify editable installation by running `pip install -e .`
- [X] T012 [US1] Run integration test for CLI subcommands in `tests/integration/test_cli.py`

## Phase 4: User Story 2 - Spec-Kit Integration Config (Priority: P2)
**Goal**: Automatically detect and prepare the integration with `spec-kit`.
**Independent Test**: Verify `ConstitutionManager` correctly identifies `.specify/memory/constitution.md`.

- [X] T013 [P] [US2] Create unit tests for `ConstitutionManager` in `tests/unit/test_manager.py`
- [X] T014 [US2] Extend `ConstitutionManager` in `src/spec_craft/core/manager.py` to handle `.specify` path discovery
- [X] T015 [US2] Add integration test for spec-kit detection in `tests/integration/test_integration.py`

## Phase 5: Polish
- [X] T016 Ensure all source files have appropriate docstrings and type hints
- [X] T017 Final verification of all success criteria in `specs/001-project-foundation-init/spec.md`

## Dependencies
- US1 (Environment Setup) is the foundation and must be completed first.
- US2 (Spec-Kit Integration) depends on US1's directory structure.

## Parallel Execution Examples
- T005, T006, T008 can be worked on in parallel once T003 is complete.
- T013 can be worked on in parallel with US1 tasks once core structure is established.
