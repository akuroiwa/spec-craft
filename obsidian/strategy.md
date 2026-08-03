# Spec-Craft Strategic Roadmap

## Core Philosophy
Spec-Craft is built on **Spec-Driven Development (SDD)**.
- **Strategy (Obsidian)**: Defines the "What" and "Why". It is the project's soul.
- **Tactics (spec-kit)**: Defines the "How". It handles iterative implementation cycles.

## Current Milestone: v0.1.5 Reached

The foundation of Spec-Craft is stable and the MCP prompt layer has been significantly improved.

### What's new since v0.1.2
- **Obsidian CLI Integration** (v0.1.5): When writing files to `obsidian/`, the AI now checks for the `obsidian` CLI and uses it to generate proper YAML front matter. Falls back to plain Markdown with manually-injected front matter if Obsidian is unavailable or declined.
- **Prompt Clarity** (v0.1.4): Rewrote `BOOT_TACTICAL_KNOWLEDGE` to eliminate Gemini CLI misidentification of spec-kit slash commands as shell commands, mandatory TOML/SKILL.md reading before any SDD phase, and RST CJK inline markup rules.
- **Multi-Agent Detection** (v0.1.3): `detector.py` now identifies Antigravity CLI automatically.

### Established Capabilities (v0.1.2)
- Multi-domain generation: 2D (SVG), 3D (Blender/Bonkei), CAD (JSCAD), BIM (Bonsai).
- Visual Feedback: AI can "see" assets via SVG projections.
- Isolated Editing: AI-dedicated Emacs sandbox with LSP/Linting.
- Transparency: "Suggest-and-Confirm" workflow for secure operations.

## Known Issues to Address (Phase 014)

Based on a detailed architecture review (2026-07-30):

1. **`EmacsManager.edit_file()` always saves** (`save-buffer` is forced). A read-only inspection method (`eval_in_buffer`) is needed so the AI can query Flymake diagnostics and xref definitions without modifying files.
2. **`init.el` startup race condition**: The 1-second sleep after `emacs --daemon` is insufficient when `package-install-selected-packages` fetches packages from the network. A health-check polling loop is needed in `start_daemon()`.
3. **`init.el` missing `global-auto-revert-mode`**: When the AI edits a file directly and Emacs has the same buffer open, the in-memory buffer becomes stale and can overwrite the AI's changes on next `save-buffer`. Adding `(global-auto-revert-mode 1)` prevents this.
4. **`parser.py` code-block heading misdetection**: The MULTILINE regex `^#{1,6}` matches `# comment` lines inside fenced code blocks. This splits sections incorrectly. A code-fence state-tracker or AST-based approach is needed.

## Transition Note: Antigravity CLI / Multi-Agent Workflows
This project supports multi-agent SDD workflows (Antigravity CLI, Gemini CLI, Claude Code, Aider).

**Instruction for the AI Agent**:
1. Read the full tactical history in the `specs/` directory (Phases 001-014).
2. Review the technical manual at [https://spec-craft.readthedocs.io/](https://spec-craft.readthedocs.io/).
3. Use `spec-craft check-env` to verify the local environment.
4. Continue using the SDD workflow (Specify → Plan → Tasks → Implement).
5. Before writing any file to `obsidian/`, run `obsidian help` to detect Obsidian CLI availability (see `BOOT_TACTICAL_KNOWLEDGE` Section 6).

## Future Roadmap
- Deeper integration with architectural analysis tools (Bonsai/BlenderBIM).
- `obsidian.yaml` command mapping: add `obsidian-bonsai` entry for `trigger_bonsai_build`.
- Extension support for generative music and video.
- Real-time synchronization between Obsidian canvases and tactical tasks.
- SVG driver: handle `<tspan>` nested text replacement without layout breakage.
