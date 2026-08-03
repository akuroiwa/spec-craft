# Data Model & Classes: Emacs Inspect and Parser Fix

This document defines the key classes, methods, and configurations changed or added in this feature.

## 1. Emacs Sandbox Components

### `EmacsManager` (`src/spec_craft/core/emacs.py`)
Responsible for managing the Emacs daemon lifespan and communicating via `emacsclient`.

#### Added Methods:
* `eval_in_buffer(self, file_path: str, elisp_action: str) -> str`
  - **Purpose**: Runs a read-only or inspection Elisp command on a buffer without saving it to disk.
  - **Logic**:
    1. Resolve `abs_path = os.path.abspath(file_path)`.
    2. Format Elisp command:
       `f'(with-current-buffer (find-file-noselect "{abs_path}") (revert-buffer t t) {elisp_action})'`
    3. Call `self.execute_command(full_command)` and return output.

#### Modified Methods:
* `start_daemon(self)`
  - **Purpose**: Headlessly spawns `emacs --daemon` and waits for socket initialization.
  - **Logic**:
    1. If `self.is_daemon_running()` is True, return immediately.
    2. Spawn subprocess `emacs --init-directory ... --daemon=... --no-window-system`.
    3. Start a polling loop:
       - Every `poll_interval` (default 0.5s), call `self.is_daemon_running()`.
       - If ready, return `True`.
       - If elapsed time exceeds `max_wait` (default 30s), raise `RuntimeError`.

### `init.el` (`src/spec_craft/data/emacs/init.el`)
The startup configuration file for the sandboxed Emacs instance.

#### Added Configuration:
* `(global-auto-revert-mode 1)`
  - **Purpose**: Automatically reload file buffers when their corresponding files are modified on disk by external tools (e.g. standard Python `open().write()`).

---

## 2. Storyboard Parser Components

### `StoryboardParser` (`src/spec_craft/core/parser.py`)
Parses Obsidian markdown files into structured sections.

#### Modified Methods:
* `parse(self, relative_path: str) -> Storyboard`
  - **Purpose**: Splits markdown content into `Section` objects.
  - **Fenced Code Block Handling**:
    1. Scan content for code fences (` ``` `).
    2. Extract all matching blocks: `re.compile(r"(```[a-zA-Z0-9_-]*\n.*?^```)", re.MULTILINE | re.DOTALL)`
    3. Replace blocks with placeholders: `__CODE_BLOCK_{index}__`.
    4. Run `header_regex.split(substituted_content)`.
    5. Reconstruct sections and replace `__CODE_BLOCK_{index}__` back with original block content in the section bodies.
