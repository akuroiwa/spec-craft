# Tasks: Emacs Inspect and Parser Fix

**Input**: Design documents from `/specs/014-emacs-inspect-and/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and check workspace readiness

- [ ] T001 Verify project structure and plan files in specs/014-emacs-inspect-and/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Prepare shared mock assets for unit testing

- [ ] T002 Create a directory or template file for test cases if needed (in tests/unit/ or mock files)

---

## Phase 3: User Story 1 - AI queries Flymake diagnostics without saving (Priority: P1) 🎯 MVP

**Goal**: Enable read-only inspection in the Emacs sandbox via `eval_in_buffer`.

**Independent Test**: Verify calling `eval_in_buffer` on a test file returns data, executes `(revert-buffer t t)`, and does not modify the target file's mtime on disk.

### Implementation for User Story 1

- [ ] T003 Implement `eval_in_buffer(self, file_path: str, elisp_action: str) -> str` in `src/spec_craft/core/emacs.py`
- [ ] T004 [P] [US1] Create unit tests in `tests/unit/test_emacs.py` to verify `eval_in_buffer` does not write changes to disk and correctly reflects on-disk changes.

**Checkpoint**: User Story 1 is fully functional and testable.

---

## Phase 4: User Story 2 - Emacs daemon starts reliably (Priority: P1)

**Goal**: Avoid connection race conditions by checking `is_daemon_running` in a loop during `start_daemon`.

**Independent Test**: Verify `start_daemon` successfully blocks until the socket is active, and times out gracefully if the daemon fails to bind the socket.

### Implementation for User Story 2

- [ ] T005 [US2] Update `start_daemon` in `src/spec_craft/core/emacs.py` to poll `is_daemon_running` with a timeout (default 30s) and poll interval (0.5s).
- [ ] T006 [P] [US2] Add unit tests in `tests/unit/test_emacs.py` to verify daemon polling and timeout logic.

**Checkpoint**: User Story 2 is fully functional.

---

## Phase 5: User Story 3 - Emacs buffer auto-refreshes (Priority: P2)

**Goal**: Ensure files edited directly by AI are automatically reloaded in Emacs buffers.

**Independent Test**: Verify buffers in the sandboxed Emacs instance revert changes automatically after file-writes.

### Implementation for User Story 3

- [ ] T007 [US3] Add `(global-auto-revert-mode 1)` to `src/spec_craft/data/emacs/init.el`

**Checkpoint**: User Story 3 is functional.

---

## Phase 6: User Story 4 - Storyboard parser ignores code block headings (Priority: P2)

**Goal**: Prevent comments (prefixed with `#`) inside markdown code fences from being parsed as document headings.

**Independent Test**: Verify parsing a markdown file with `# comments` inside a python code fence does not produce incorrect section objects.

### Implementation for User Story 4

- [ ] T008 [US4] Modify `parse` method in `src/spec_craft/core/parser.py` to replace fenced code blocks with placeholders during heading detection and restore them afterward.
- [ ] T009 [P] [US4] Add unit tests in `tests/unit/test_parser.py` containing code fences with comment lines.

**Checkpoint**: User Story 4 is functional.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Verify the complete feature changes.

- [ ] T010 [P] Run verification scripts in `quickstart.md` and check results.
- [ ] T011 Run `uv run pytest` to ensure all 47+ tests pass.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup.
- **User Stories (Phases 3-6)**: Depend on Foundational.
  - Phase 3 (US1) and Phase 4 (US2) are P1 priorities and should be implemented first.
  - Phase 5 (US3) depends on US1/US2 logic.
  - Phase 6 (US4) is independent of Emacs features but should be implemented sequentially.
- **Polish (Phase 7)**: Depends on all user stories being complete.
