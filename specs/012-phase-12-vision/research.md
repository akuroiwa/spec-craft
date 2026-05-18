# Research: Vision Feedback & Isolated Editing

## Decisions

### 1. Blender Freestyle SVG Integration
- **Decision**: Programmatically enable `render_freestyle_svg` in generated scripts.
- **Rationale**: This addon is bundled with Blender 4.x and provides clean 2D vector output of 3D geometry. SVG is token-efficient and perfect for AI analysis compared to raster renders.
- **Alternatives**: Rendering PNGs (rejected due to high noise/token usage).

### 2. Emacs Sandbox Isolation
- **Decision**: Use `emacs --init-directory <path> --daemon=<name>` to start project-specific sessions.
- **Rationale**: Ensures the AI uses a controlled configuration without affecting the user's `~/.emacs.d`. `--init-directory` (Emacs 29+) is the cleanest way to redirect config.
- **Alternatives**: Setting `HOME` environment variable (complex, may affect other tools).

### 3. LSP & Linting Strategy
- **Decision**: Use `eglot` as the default LSP client and `flymake` for real-time diagnostics.
- **Rationale**: Both are built into modern Emacs, minimizing the need for external package downloads in the sandbox.
- **Alternatives**: `lsp-mode` and `flycheck` (rejected as they require more setup/downloads).

## Best Practices
- **BIM/CAD Consistency**: When rendering SVG from Blender, use standard views (Top, Side) to help the AI map 2D data to 3D specs.
- **Atomic Edits**: Use `emacsclient --eval` to send precise Elisp commands rather than interactive keyboard simulation.
