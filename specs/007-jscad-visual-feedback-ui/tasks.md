# Tasks: JSCAD Visual Feedback Loop and 3D Preview UI

## Implementation Strategy
We will implement the visual feedback loop and 3D preview UI by first established the actual JSCAD driver using `npx`, then creating the static web assets for the Three.js viewer, and finally building the local web server to host the preview. Verification will include testing the driver's multi-format output and the server's ability to serve bundled resources.

## Phase 1: Setup
- [X] T001 Create `src/spec_craft/static/` and `src/spec_craft/core/ui/` directories
- [X] T002 Initialize `src/spec_craft/static/index.html` with Three.js viewer shell
- [X] T003 Initialize `src/spec_craft/static/viewer.js` with STL loading logic

## Phase 2: Foundational
- [X] T004 [P] Update `src/spec_craft/core/drivers/cad.py` to use actual `npx @jscad/cli` commands
- [X] T005 [P] Implement `CADDriver` support for SVG projection output
- [X] T006 Implement `PreviewServer` using `http.server` in `src/spec_craft/core/ui/server.py`

## Phase 3: User Story 1 - Visual Feedback Loop (Priority: P1)
**Goal**: Generate a visual representation (SVG) of CAD models for AI analysis.
**Independent Test**: Trigger a CAD build and verify that both .stl and .svg files exist in `build/cad/`.

- [X] T007 [US1] Extend `trigger_cad_build` in `src/spec_craft/mcp/server.py` to accept `formats` argument
- [X] T008 [US1] Update `CADDriver` unit tests in `tests/unit/test_cad_driver.py` to verify multi-format output
- [X] T009 [US1] Add integration test for SVG visual feedback loop in `tests/integration/test_visual_feedback.py`

## Phase 4: User Story 2 - Interactive 3D Preview (Priority: P2)
**Goal**: Preview generated 3D models in a web browser via local server.
**Independent Test**: Run `spec-craft browse` and verify the browser opens with the viewer.

- [X] T010 [US2] Implement `spec-craft browse` command in `src/spec_craft/main.py` using `webbrowser` module
- [X] T011 [US2] Refine `index.html` and `viewer.js` to handle STL loading via query parameters
- [X] T012 [US2] Add unit tests for `PreviewServer` resource resolution in `tests/unit/test_ui_server.py`
- [X] T013 [US2] Verify `spec-craft browse` starts the server on the correct port and serves `build/` assets

## Phase 5: Polish
- [X] T014 Ensure proper error handling for environments missing Node.js or `npx`
- [X] T015 Final verification of all SC-001 to SC-004 criteria in `specs/007-jscad-visual-feedback-ui/spec.md`
- [X] T016 Update documentation (docs/ and README.md) with `browse` command usage

## Dependencies
- US1 (Visual Feedback) depends on T004 and T005 (Updated CADDriver).
- US2 (Interactive Preview) depends on T006 (PreviewServer) and Phase 1 (Web Assets).

## Parallel Execution Examples
- T004, T005, and T006 can be worked on in parallel once T001 is complete.
- T008 and T012 (Unit tests) can be worked on in parallel.
