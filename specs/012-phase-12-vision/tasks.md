# Tasks: Vision Feedback and Isolated Editing Environment

## Implementation Strategy
We will extend Spec-Craft with advanced AI assistance capabilities by first establishing the isolated Emacs environment and enhancing the Blender driver for visual feedback. We will then implement the MCP tools for headless rendering and editing. The final stage will focus on robust environment checking to ensure users have the necessary external tools (Emacs 29+, Blender addons).

## Phase 1: Setup
- [X] T001 Create `src/spec_craft/core/emacs.py` for daemon and client management
- [X] T002 Create `src/spec_craft/data/emacs/` directory for configuration templates
- [X] T003 [P] Define `init.el` template with `eglot`, `flymake`, and `python-ts-mode` in `src/spec_craft/data/emacs/init.el`

## Phase 2: Foundational
- [X] T004 Update `BlenderDriver` in `src/spec_craft/core/drivers/blender.py` to support Freestyle SVG code injection
- [X] T005 Implement `EmacsManager` class with daemon lifecycle and `emacsclient` execution in `src/spec_craft/core/emacs.py`
- [X] T006 [P] Update `WorkspaceDetector` in `src/spec_craft/core/detector.py` to detect Emacs version and Blender Freestyle addon status

## Phase 3: User Story 1 - Visual Verification of 3D Assets (Priority: P1)
**Goal**: Enable AI to verify 3D geometry using Freestyle SVG projections.
**Independent Test**: Trigger a render and verify the SVG existence and content.

- [X] T007 [US1] Implement `render_blender_svg` tool logic in `src/spec_craft/mcp/server.py`
- [X] T008 [US1] Register `render_blender_svg` tool in `src/spec_craft/mcp/server.py`
- [X] T009 [P] [US1] Add integration test for Blender SVG rendering in `tests/integration/test_blender_vision.py`

## Phase 4: User Story 2 - High-Precision Code Editing (Priority: P2)
**Goal**: Provide an isolated Emacs environment for AI-assisted coding with LSP.
**Independent Test**: Successfully run a headless Elisp command via `edit_with_emacs`.

- [X] T010 [US2] Implement `setup_emacs_sandbox` tool in `src/spec_craft/mcp/server.py`
- [X] T011 [US2] Implement `edit_with_emacs` tool in `src/spec_craft/mcp/server.py`
- [X] T012 [P] [US2] Add unit tests for `EmacsManager` in `tests/unit/test_emacs.py`

## Phase 5: User Story 3 - Comprehensive Prerequisite Checking (Priority: P3)
**Goal**: Automatically detect missing tools for vision and editing features.
**Independent Test**: Verify `check-env` output on a system missing Emacs.

- [X] T013 [US3] Register `ai_emacs_guide` prompt in `src/spec_craft/mcp/server.py`
- [X] T014 [US3] Finalize `check_environment` tool registration to include new checks

## Phase 6: Polish
- [X] T015 Update root `README.md` with new vision feedback and Emacs sandbox usage
- [X] T016 Final verification of all success criteria (SC-001 to SC-004) in Phase 12 spec

## Dependencies
- US1 (Vision) depends on `BlenderDriver` updates (T004).
- US2 (Editing) depends on `EmacsManager` (T005).
- All stories benefit from the updated `check_environment` (T006).

## Parallel Execution Examples
- T003 (init.el) and T004 (BlenderDriver) can be worked on in parallel.
- T009 (Vision tests) and T012 (Emacs tests) can be developed simultaneously.
