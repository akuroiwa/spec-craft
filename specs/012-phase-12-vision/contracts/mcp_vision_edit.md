# MCP Contract: Vision & Isolated Editing

## Tools

### `render_blender_svg`
- **Purpose**: Render a 3D scene to SVG using Blender Freestyle for AI analysis.
- **Input**: `script_path` (str), `output_name` (str).
- **Output**: Path to the generated SVG.

### `setup_emacs_sandbox`
- **Purpose**: Initialize a project-specific Emacs environment.
- **Input**: None.
- **Output**: JSON status of the sandbox and daemon.

### `edit_with_emacs`
- **Purpose**: Execute Elisp commands via emacsclient to modify or analyze files.
- **Input**: `command` (str), `file_path` (Optional[str]).
- **Output**: Command output or error log.

## Prompts

### `ai-emacs-guide`
- **Role**: Guidance for using the isolated Emacs environment (Lisp patterns, Eglot usage).
