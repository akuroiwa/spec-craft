# Tasks: Final Refinement of JSCAD/Bonsai Drivers and Release Preparation

## Implementation Strategy
We will complete the Spec-Craft refinement by first updating the core drivers and environment detection logic to handle the specific technical requirements of JSCAD v2 and the Bonsai API. Simultaneously, we will finalize the Japanese documentation. Once verified locally, we will perform a staging release to Test PyPI to ensure the packaging and distribution pipeline is robust.

## Phase 1: Setup
- [ ] T001 Add `twine` to dev dependencies using `uv add --dev twine` for release staging

## Phase 2: Foundational
- [ ] T002 [P] Enhance `check_environment` in `src/spec_craft/core/detector.py` to detect `@jscad` npm packages and the Bonsai Blender add-on

## Phase 3: User Story 1 - Reliable JSCAD/Bonsai Builds (Priority: P1)
**Goal**: Ensure correct code generation and asset output for CAD and BIM domains.
**Independent Test**: Trigger CAD build and verify both STL and SVG; trigger Bonsai build and verify `import bonsai` usage.

- [ ] T003 [P] [US1] Update `CADDriver.build` in `src/spec_craft/core/drivers/cad.py` to ensure sequential npx execution for multiple formats
- [ ] T004 [US1] Update `BonsaiDriver.generate_ifc_script` in `src/spec_craft/core/drivers/bonsai.py` to use latest Bonsai API (import bonsai, create_project)
- [ ] T005 [US1] Refine `CAD_GUIDE` and `BONSAI_GUIDE` in `src/spec_craft/mcp/prompts.py` with corrected module imports and initialization logic
- [ ] T006 [US1] Run unit and integration tests for CAD and Bonsai drivers to verify technical correctness

## Phase 4: User Story 2 - Complete Japanese Manual (Priority: P2)
**Goal**: 100% localization of the manual in Japanese.
**Independent Test**: Run `make ja` and verify all sections are translated in `docs/_build/html/ja/`.

- [ ] T007 [P] [US2] Complete translations for `installation.md` and `domain-guides.md` in `docs/source/locale/ja/LC_MESSAGES/`
- [ ] T008 [US2] Refine `strategy.md` translations to ensure consistent terminology (Strategy/Tactics)
- [ ] T009 [US2] Generate and verify the full Japanese manual build using Sphinx

## Phase 5: User Story 3 - Staging Release on Test PyPI (Priority: P3)
**Goal**: Verify packaging and distribution on Test PyPI.
**Independent Test**: Install the package from Test PyPI and verify `spec-craft --version`.

- [ ] T010 [US3] Finalize metadata and versioning in `pyproject.toml`
- [ ] T011 [US3] Execute `uv build` and verify distribution integrity with `twine check dist/*`
- [ ] T012 [US3] Upload to Test PyPI and perform a test installation in a clean environment

## Phase 6: Polish
- [ ] T013 Update root `README.md` with final release notes and a "How to Contribute" section
- [ ] T014 Final verification of all SC-001 to SC-004 criteria in Phase 11 spec

## Dependencies
- US1 (Builds) and US2 (Manual) are independent and can be worked on in parallel.
- US3 (Staging) depends on the successful verification of US1 and US2.

## Parallel Execution Examples
- T003 (CAD refinement) and T007 (Documentation translation) can be performed in parallel.
- T002 (Environment detection) can be developed alongside T004 (Bonsai refinement).
