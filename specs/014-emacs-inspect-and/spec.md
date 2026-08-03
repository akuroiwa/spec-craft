# Feature Specification: Emacs Inspect and Parser Fix

**Feature Branch**: `014-emacs-inspect-and`

**Created**: 2026-07-31

**Status**: Draft

**Input**: User description: "Emacs inspect and parser fix."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - AI queries Flymake diagnostics without saving (Priority: P1)

An AI agent opens a Python file in the Emacs sandbox, reads Flymake diagnostic
results (errors, warnings) to understand code health, and then hands the
corrected content back to the AI's own file-write tool — all without Emacs
touching the file on disk.

**Why this priority**: The current `edit_file()` method forces `save-buffer`
even during read-only inspection. This is the root cause identified in the
architecture review. Fixing it unlocks safe LSP/Flymake queries.

**Independent Test**: Can be tested by calling `eval_in_buffer` on a file that
contains a deliberate syntax error and verifying that Flymake diagnostics are
returned and the file modification time has NOT changed.

**Acceptance Scenarios**:

1. **Given** a Python file with a known syntax error is present, **When** the AI
   calls `eval_in_buffer(file_path, "(flymake-diagnostics)")`, **Then** a
   non-empty list of diagnostics is returned and the file is not modified on disk.
2. **Given** the Emacs daemon is running with Eglot active, **When** the AI calls
   `eval_in_buffer` with an xref query, **Then** the definition location is
   returned and no save occurs.

---

### User Story 2 - Emacs daemon starts reliably even with slow package init (Priority: P1)

When `start_daemon()` is called for the first time, the daemon waits until the
Emacs server socket is fully ready before returning, regardless of how long
`package-install-selected-packages` takes.

**Why this priority**: The fixed 1-second sleep causes intermittent
`emacsclient` connection failures on slow networks or first-time installs. This
is a reliability blocker.

**Independent Test**: Can be tested by deleting the sandbox directory and
calling `start_daemon()` while on a metered connection; the call must succeed
and `is_daemon_running()` must return `True` immediately after.

**Acceptance Scenarios**:

1. **Given** no sandbox exists, **When** `start_daemon()` is called, **Then** it
   polls `is_daemon_running()` up to a configurable timeout and returns `True`
   only after the socket is ready.
2. **Given** the daemon startup takes more than 1 second, **When** `start_daemon()`
   is called, **Then** it does NOT return before the socket is ready (no premature
   `emacsclient` failure).

---

### User Story 3 - Emacs buffer auto-refreshes after AI direct file edit (Priority: P2)

When the AI writes a file directly (without Emacs) and then calls any Emacs
inspection tool, Emacs automatically reloads the buffer from disk so that the
analysis reflects the AI's latest changes and not a stale in-memory copy.

**Why this priority**: Without `global-auto-revert-mode`, a subsequent
`save-buffer` in Emacs would silently overwrite the AI's edits with the old
buffer content.

**Independent Test**: AI writes content X to a file, then calls `eval_in_buffer`
which internally reads the buffer text; the returned text must equal X, not the
original content.

**Acceptance Scenarios**:

1. **Given** `global-auto-revert-mode` is enabled in `init.el`, **When** the AI
   writes new content to a file that Emacs has open as a buffer, **Then**
   subsequent Emacs reads of that buffer return the new content.
2. **Given** the AI edits a file and immediately calls an LSP query, **Then** the
   LSP analysis is based on the updated file, not the previous buffer state.

---

### User Story 4 - Storyboard parser ignores `#` inside code fences (Priority: P2)

When `StoryboardParser.parse()` processes an Obsidian Markdown file that
contains fenced code blocks with `#`-prefixed comment lines (e.g., Python or
bash comments), those comment lines are not mistaken for Markdown headings.

**Why this priority**: Incorrect section splitting corrupts the structured
`Storyboard` object, causing downstream MCP tools (`read_storyboard`) to return
wrong section content to the AI.

**Independent Test**: Parse a Markdown file containing a fenced bash block with
`# This is a comment` inside it; the resulting `Storyboard.sections` list must
not include a section whose title is "This is a comment".

**Acceptance Scenarios**:

1. **Given** a Markdown file with a ```` ```python ```` block containing `# comment`,
   **When** `StoryboardParser.parse()` is called, **Then** the number of returned
   sections matches the actual Markdown heading count, not the heading count plus
   code-block comment count.
2. **Given** nested code fences are present, **When** parsed, **Then** all content
   inside the outermost fence is treated as literal text.

---

### Edge Cases

- What happens when the Emacs daemon crashes mid-inspection? `eval_in_buffer`
  must attempt one restart before raising an error.
- How does `start_daemon()` behave when the timeout is exceeded? It must raise a
  clear `RuntimeError` with the elapsed wait time.
- What if a Markdown file contains an unclosed code fence? The parser must treat
  the rest of the file as fence content rather than scanning for headings.
- What if `global-auto-revert-mode` conflicts with unsaved user edits in an
  interactive Emacs session sharing the same socket? (Out of scope — the sandbox
  socket is dedicated to spec-craft.)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `EmacsManager` MUST expose an `eval_in_buffer(file_path, elisp_action)` method that executes Elisp without calling `save-buffer`.
- **FR-002**: `eval_in_buffer` MUST prepend `(revert-buffer t t)` before the user-supplied Elisp action to ensure the buffer reflects the current disk state.
- **FR-003**: `start_daemon()` MUST poll `is_daemon_running()` in a loop with configurable `max_wait` (default 30 s) and `poll_interval` (default 0.5 s) instead of using a fixed `time.sleep(1)`.
- **FR-004**: `start_daemon()` MUST raise `RuntimeError` with an informative message if the daemon is not ready within `max_wait` seconds.
- **FR-005**: `data/emacs/init.el` MUST include `(global-auto-revert-mode 1)` so Emacs buffers automatically reload when files are modified externally.
- **FR-006**: `StoryboardParser.parse()` MUST track code-fence state (opening and closing triple-backtick lines) and exclude content inside fences from heading detection.
- **FR-007**: The existing `edit_file()` method MUST be preserved unchanged for backward compatibility (it is used when the AI genuinely wants to edit and save via Emacs).

### Key Entities

- **`EmacsManager`**: Core class in `src/spec_craft/core/emacs.py`. Gains `eval_in_buffer()` method and improved `start_daemon()`.
- **`init.el`**: Emacs init file in `src/spec_craft/data/emacs/init.el`. Gains `global-auto-revert-mode`.
- **`StoryboardParser`**: Core class in `src/spec_craft/core/parser.py`. Gains code-fence-aware heading detection.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `eval_in_buffer` returns Flymake diagnostic data for a file with a
  known syntax error and the file modification time is unchanged (verified by
  `os.path.getmtime` before and after).
- **SC-002**: `start_daemon()` succeeds in under 30 seconds on a clean sandbox
  and returns `True` without any `emacsclient` connection errors.
- **SC-003**: After the AI writes new content to a file, an `eval_in_buffer` call
  that reads the buffer text returns the new content (not the pre-write content).
- **SC-004**: `StoryboardParser.parse()` produces the correct section count when
  given a Markdown file containing fenced code blocks with `#` lines — verified
  by unit test.
- **SC-005**: All 47 existing tests continue to pass after the changes.

## Assumptions

- The Emacs sandbox socket is dedicated to spec-craft and is not shared with the
  user's interactive Emacs session, so `global-auto-revert-mode` will not
  disrupt any interactive editing.
- The Python `markdown` AST library is NOT introduced as a new dependency; the
  code-fence fix uses a lightweight state-tracking loop within the existing
  `parser.py` code.
- `eval_in_buffer` is intended for headless inspection only; the AI continues to
  use its own file-write tools for content generation and only calls Emacs for
  LSP/Flymake queries.
- Eglot / pyright must already be installed in the environment for LSP-based
  acceptance scenarios (SC-001 LSP variant); Flymake-only scenarios work without
  LSP.
