# Tasks: spec-kit Extension Interface and 3D Integration via Blender

## Implementation Strategy
We will complete the spec-craft ecosystem by establishing the Blender 3D driver and the official spec-kit extension interface. The focus is on translating "Strategic" Bonkei descriptions into "Tactical" Blender Python scripts and providing a unified slash-command interface for users.

## Phase 1: Setup
- [X] T001 Create `extension/` directory in the root and initialize `extension/extension.yml`
- [X] T002 Create `src/spec_craft/core/drivers/blender.py` for 3D generation logic

## Phase 2: Foundational
- [X] T003 Implement `BlenderDriver` class in `src/spec_craft/core/drivers/blender.py` with scene scripting capabilities
- [X] T004 Define `BLENDER_GUIDE` constant with Bonkei logic in `src/spec_craft/mcp/prompts.py`

## Phase 3: User Story 1 - spec-kit Extension Integration (Priority: P1)
**Goal**: Use spec-craft features via spec-kit slash commands.
**Independent Test**: Verify `/speckit.obsidian-analyze` executes the `read_storyboard` MCP tool.

- [X] T005 [P] Define slash command mappings in `extension/extension.yml` (obsidian-analyze, obsidian-build)
- [X] T006 Implement `trigger_full_build` tool in `src/spec_craft/mcp/server.py` to coordinate all drivers
- [X] T007 Add integration test for extension command recognition in `tests/integration/test_extension.py`

## Phase 4: User Story 2 - Blender 3D Generation (Priority: P2)
**Goal**: Generate Blender Python scripts from Obsidian scene specs.
**Independent Test**: Trigger `generate_blender_script` and verify the output contains valid `bpy` calls.

- [X] T008 [P] [US2] Create unit tests for `BlenderDriver` in `tests/unit/test_blender_driver.py`
- [X] T009 [US2] Register `generate_blender_script` tool in `src/spec_craft/mcp/server.py`
- [X] T010 [US2] Register `blender_3d_guide` prompt in `src/spec_craft/mcp/server.py`
- [X] T011 [US2] Add integration test for 3D build path in `tests/integration/test_build_pipeline.py`

## Phase 5: User Story 3 - Full Pipeline Validation (Priority: P3)
**Goal**: Verify the entire "Strategy to Asset" flow.
**Independent Test**: Run a full build that generates SVG, STL, and .py artifacts.

- [X] T012 [US3] Create a comprehensive "Gold Master" integration test in `tests/integration/test_full_pipeline.py`
- [X] T013 [US3] Verify hierarchical organization for 3D scripts in `build/3d/` via `BuildManager`

## Phase 6: Polish
- [X] T014 Ensure the `extension.yml` is properly formatted and ready for local installation
- [X] T015 Final verification of all success criteria in `specs/005-extension-interface-blender/spec.md`
- [X] T016 Update root `README.md` with instructions for extension installation and Blender usage

## Dependencies
- US1 (Extension) depends on tools registered in previous phases.
- US2 (Blender) depends on T003 (BlenderDriver).
- US3 (Pipeline) depends on all drivers being operational.

## Parallel Execution Examples
- T005 (Manifest) and T008 (Driver tests) can be worked on in parallel.
- T010 (Prompt) and T009 (Tool) registration can be done independently.
