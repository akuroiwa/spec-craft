# Tasks: Multilingual SVG Pipeline and Multi-domain Build Integration

## Implementation Strategy
We will implement the generation pipeline by first establishing the build management infrastructure, then creating the specialized drivers for SVG and CAD. The `BuildManager` will ensure that all assets are correctly organized by domain and language. Testing will involve unit tests for the XML manipulation logic and integration tests for the full build cycle.

## Phase 1: Setup
- [X] T001 Update `pyproject.toml` to include `lxml` dependency in the root directory
- [X] T002 Sync dependencies using `uv sync` in the root directory
- [X] T003 Create directory structure: `src/spec_craft/core/drivers/` and `templates/`

## Phase 2: Foundational
- [X] T004 Implement `BuildManager` for directory coordination in `src/spec_craft/core/build.py`
- [X] T005 [P] Create `BuildAsset` Pydantic model for metadata tracking in `src/spec_craft/core/build.py`

## Phase 3: User Story 1 - Multilingual SVG Generation (Priority: P1)
**Goal**: Generate translated SVGs from templates and Obsidian dictionaries.
**Independent Test**: Trigger an SVG build and verify the text replacement in the output file.

- [X] T006 [P] [US1] Create unit tests for `SVGDriver` in `tests/unit/test_svg_driver.py`
- [X] T007 [US1] Implement `SVGDriver` with lxml-based text injection in `src/spec_craft/core/drivers/svg.py`
- [X] T008 [US1] Register `trigger_svg_build` tool in `src/spec_craft/mcp/server.py`
- [X] T009 [US1] Add integration test for SVG build cycle in `tests/integration/test_build_pipeline.py`

## Phase 4: User Story 2 - Parametric CAD Generation (Priority: P2)
**Goal**: Generate STL files from JSCAD code specifications.
**Independent Test**: Trigger a CAD build and verify the existence of .js and .stl files in build/cad/.

- [X] T010 [US2] Implement `CADDriver` wrapping `jscad-tool.js` in `src/spec_craft/core/drivers/cad.py`
- [X] T011 [US2] Register `trigger_cad_build` tool in `src/spec_craft/mcp/server.py`
- [X] T012 [US2] Add integration test for CAD build cycle in `tests/integration/test_build_pipeline.py`

## Phase 5: User Story 3 - Build Management (Priority: P3)
**Goal**: Automatically organize the build directory by domain and language.
**Independent Test**: Run multiple builds and verify the directory tree matches the expected hierarchy.

- [X] T013 [US3] Extend `BuildManager` to handle hierarchical path generation (domain/lang) in `src/spec_craft/core/build.py`
- [X] T014 [US3] Define and register `build-organization-guide` prompt in `src/spec_craft/mcp/prompts.py` and `server.py`

## Phase 6: Polish
- [X] T015 Ensure strict path validation for build outputs to prevent directory traversal
- [X] T016 Final verification of all success criteria in `specs/004-multilingual-svg-pipeline/spec.md`

## Dependencies
- US1 (SVG) depends on T004 (BuildManager).
- US2 (CAD) depends on T004 (BuildManager).
- US3 (Management) depends on US1 and US2 implementation details.

## Parallel Execution Examples
- T005, T006 can be done in parallel once T003 is complete.
- T007 and T010 (Drivers) can be worked on independently.
