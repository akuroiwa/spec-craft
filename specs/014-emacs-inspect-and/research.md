# Research: Emacs Inspect and Parser Fix

## Decision 1: `eval_in_buffer` Implementation
- **Selected Approach**: Implement `eval_in_buffer(self, file_path: str, elisp_action: str) -> str` in `EmacsManager`.
- **Details**:
  - The Elisp command will be:
    `'(with-current-buffer (find-file-noselect "{abs_path}") (revert-buffer t t) {elisp_action})'`
  - Since this does not call `(save-buffer)`, the file remains clean on disk.
  - Adding `(revert-buffer t t)` explicitly guarantees that any modification done externally (e.g. by AI's own write tool) is loaded into the buffer before the action runs.
- **Alternatives Considered**: Automatically closing the buffer (kill-buffer) after every action. Rejected because Eglot (LSP) connection and cache are lost, making subsequent calls slower.

## Decision 2: `start_daemon` Polling Loop
- **Selected Approach**: Poll `self.is_daemon_running()` inside `start_daemon()` in a while loop.
- **Details**:
  - Keep trying for up to 30 seconds (configurable, e.g., `max_wait=30`, `poll_interval=0.5`).
  - If it succeeds, return `True` immediately.
  - If 30 seconds pass without success, raise `RuntimeError("Emacs daemon failed to start within 30 seconds.")`.
- **Alternatives Considered**: Increasing `time.sleep(1)` to `time.sleep(5)`. Rejected because it introduces unnecessary static delays when the socket is ready faster, and still might fail on extremely slow initialization.

## Decision 3: `global-auto-revert-mode` in `init.el`
- **Selected Approach**: Add `(global-auto-revert-mode 1)` to the `init.el` template.
- **Details**:
  - This ensures that if the daemon keeps a file buffer open, any external modifications are immediately synchronized back into the buffer in memory.

## Decision 4: Code Block Heading Fix in `parser.py`
- **Selected Approach**: Use a regex-based substitution to temporarily replace code blocks before heading parsing, then restore them.
- **Details**:
  - Before running `header_regex.split(content)`, temporarily replace all fenced code blocks (matching ```...``` with DOTALL) with placeholders like `__CODE_BLOCK_{index}__`.
  - Perform the regular heading parsing and section splits on the placeholder-substituted content.
  - Finally, iterate over the parsed sections and replace the placeholders back with the original code blocks in `Section.content`.
  - Code Block regex: `re.compile(r"(```[a-zA-Z0-9_-]*\n.*?^```)", re.MULTILINE | re.DOTALL)`
- **Alternatives Considered**: Row-by-row scanning. Rejected because the split logic is already clean and rewriting it row-by-row increases complexity and potential bugs in heading levels.
