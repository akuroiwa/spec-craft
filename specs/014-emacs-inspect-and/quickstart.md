# Quickstart & Verification: Emacs Inspect and Parser Fix

This document provides quick code snippets and testing instructions to verify the new features.

## 1. Verifying `eval_in_buffer` and `global-auto-revert-mode`

Run the following Python script using `uv run python` inside the repository root to verify that Emacs inspects a file without saving it, and auto-refreshes when updated externally.

```python
import os
from pathlib import Path
from spec_craft.core.emacs import EmacsManager

# Setup manager
emacs = EmacsManager(Path.cwd())
emacs.ensure_sandbox()

# 1. Start daemon (uses new polling loop)
print("Starting daemon...")
emacs.start_daemon()
print("Daemon started successfully!")

# 2. Write a test file
test_file = Path("test_sandbox_file.py")
test_file.write_text("def my_func():\n    pass\n")
initial_mtime = test_file.stat().st_mtime

# 3. Read it via Emacs eval_in_buffer
print("Reading file buffer content via Emacs...")
buf_content = emacs.eval_in_buffer(str(test_file), "(buffer-substring-no-properties (point-min) (point-max))")
print("Buffer content:", repr(buf_content))

# 4. Modify the file externally
print("Modifying file on disk (simulating AI file write)...")
test_file.write_text("def my_func():\n    return 42\n")

# 5. Read again via Emacs (revert-buffer/global-auto-revert-mode should auto-update)
print("Reading again via Emacs...")
updated_buf_content = emacs.eval_in_buffer(str(test_file), "(buffer-substring-no-properties (point-min) (point-max))")
print("Updated buffer content:", repr(updated_buf_content))

# 6. Verify modification time on disk
final_mtime = test_file.stat().st_mtime
print("Is disk modification preserved?", initial_mtime != final_mtime)

# Cleanup
test_file.unlink()
emacs.stop_daemon()
```

---

## 2. Verifying Storyboard Parser

Run this script to verify that code fences are ignored by the Markdown parser:

```python
from pathlib import Path
from spec_craft.core.parser import StoryboardParser

# Create a mock storyboard with code block containing `# comment`
mock_obsidian_dir = Path("mock_obsidian")
mock_obsidian_dir.mkdir(exist_ok=True)

test_note = mock_obsidian_dir / "test_note.md"
test_note.write_text("""---
title: Mock Storyboard
---
# Main Heading

Here is some text.

```python
# This is a comment, not a heading!
def test():
    pass
```

## Sub Heading

More text here.
""")

parser = StoryboardParser(mock_obsidian_dir)
storyboard = parser.parse("test_note.md")

print("Parsed sections:")
for section in storyboard.sections:
    print(f"- Title: {repr(section.title)} (Level: {section.level})")

# Clean up
test_note.unlink()
mock_obsidian_dir.rmdir()
```

Expected output should only contain `Preamble`, `Main Heading`, and `Sub Heading`. It must **NOT** contain `This is a comment, not a heading!`.
