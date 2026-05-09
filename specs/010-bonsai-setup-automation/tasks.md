# Tasks: Bonsai (BlenderBIM) Integration and Setup Automation

## Implementation Strategy
We will complete the Spec-Craft toolkit by integrating professional architectural support via Bonsai (BlenderBIM) and automating the environmental setup. We will first implement the `BonsaiDriver` for IFC-compliant script generation, then build a robust environment checker to guide new users. Finally, we will complete the documentation translations and establish a clear path for the Test PyPI release.

## Phase 1: Setup
- [X] T001 Create `src/spec_craft/core/drivers/bonsai.py` for architectural generation logic

## Phase 2: Foundational
- [X] T002 Implement `BonsaiDriver` class with IFC entity generation logic in `src/spec_craft/core/drivers/bonsai.py`
- [X] T003 Define `BONSAI_GUIDE` and `TEST_PYPI_CHECKLIST` constants in `src/spec_craft/mcp/prompts.py`

## Phase 3: User Story 1 - Architectural Design with Bonsai (Priority: P1)
**Goal**: Support Bonsai (BlenderBIM) workflows for IFC-compliant architectural modeling.
**Independent Test**: Trigger a Bonsai script generation and verify it contains IFC wall/slab creation code.

- [X] T004 [US1] Register `bonsai_architectural_guide` prompt in `src/spec_craft/mcp/server.py`
- [X] T005 [US1] Extend `trigger_full_build` in `src/spec_craft/mcp/server.py` to include Bonsai as a capability
- [X] T006 [P] [US1] Add integration test for Bonsai script generation in `tests/integration/test_bonsai.py`

## Phase 4: User Story 2 - Proactive Setup Automation (Priority: P2)
**Goal**: Detect missing SDD prerequisites (spec-kit, obsidian, node) and suggest fixes.
**Independent Test**: Call `check_environment` and verify it identifies missing tools and provides install commands.

- [X] T007 [US2] Implement `check_environment` logic in `WorkspaceDetector` within `src/spec_craft/core/detector.py`
- [X] T008 [US2] Register `check_environment` tool in `src/spec_craft/mcp/server.py`
- [X] T009 [P] [US2] Add unit tests for environment detection in `tests/unit/test_env_check.py`

## Phase 5: User Story 3 - Production Readiness Validation (Priority: P3)
**Goal**: Verify the toolkit's readiness for Test PyPI publication.
**Independent Test**: Successfully build the package and verify the Japanese manual output.

- [ ] T010 [US3] Complete and verify all Japanese translations in `docs/source/locale/ja/LC_MESSAGES/`
- [ ] T011 [US3] Register `test_pypi_release_checklist` prompt in `src/spec_craft/mcp/server.py`
- [ ] T012 [US3] Perform a final "Mock Release" check including local wheel installation and capability tests

## Phase 6: Polish
- [ ] T013 Final verification of all success criteria (SC-001 to SC-004) in Phase 10 spec
- [ ] T014 Update root `README.md` with Bonsai support details and setup automation instructions

## Dependencies
- US1 (Bonsai) depends on T002 (BonsaiDriver).
- US2 (Setup) depends on T007 (Detector logic).
- US3 (Readiness) depends on all previous phases being stable.

## Parallel Execution Examples
- T003 (Prompts) and T002 (Driver) can be worked on in parallel.
- T009 (Unit tests) can be developed alongside T007.
