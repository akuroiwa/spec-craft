# Spec-Craft Strategic Roadmap

## Core Philosophy
Spec-Craft is built on **Spec-Driven Development (SDD)**.
- **Strategy (Obsidian)**: Defines the "What" and "Why". It is the project's soul.
- **Tactics (spec-kit)**: Defines the "How". It handles iterative implementation cycles.

## Current Milestone: v0.1.6 Reached

The foundation of Spec-Craft is stable and verified across multiple environments.

### What's new since v0.1.2
- **Emacs Inspection & Parser Resilience** (v0.1.6 / Phase 014): Added `eval_in_buffer()` for safe read-only LSP/Flymake inspections without overwriting files; implemented daemon startup polling; added `global-auto-revert-mode` to `init.el`; and fixed `StoryboardParser` code-fence heading misdetection.
- **Obsidian CLI Integration** (v0.1.5): Checks for `obsidian` CLI to generate front matter, with graceful fallback to manual front matter in plain Markdown.
- **Prompt Clarity** (v0.1.4): Refined `BOOT_TACTICAL_KNOWLEDGE` to clarify tool boundaries, slash commands, and CJK markup.
- **Multi-Agent Detection** (v0.1.3): `detector.py` automatically detects Antigravity CLI and other agents.

### Established Capabilities
- Multi-domain generation: 2D (SVG), 3D (Blender/Bonkei), CAD (JSCAD), BIM (Bonsai).
- Visual Feedback: AI can "see" assets via SVG projections.
- Isolated Editing: AI-dedicated Emacs sandbox with LSP/Linting.
- Transparency: "Suggest-and-Confirm" workflow for secure operations.

## Phase 015: Interactive Colab Notebook & Tutorial Integration

To enable hands-on evaluation, demo video creation (YouTube), and seamless user onboarding:
1. **Google Colab Notebook (`docs/notebooks/spec_craft_quickstart.ipynb`)**:
   - One-click environment setup: Ollama background server + lightweight QAT model selection (`gemma-2-2b-it` / `qwen2.5` / `gemma-4-qat`).
   - CLI Tooling: Install `uv`, `sigoden/aichat`, and `spec-craft`.
   - End-to-End SDD Workflow:
     - Step 1: Generate an Obsidian strategic feature specification via `aichat`.
     - Step 2: Parse and preview the strategic specification using `spec-craft` tools.
     - Step 3: Trigger `spec-kit` automated workflows to produce code and unit tests.
     - Step 4: Run tests and verify behavior directly within Colab.
2. **Read the Docs & Sphinx Integration**:
   - Integrated `myst-nb` into Sphinx documentation builder (`docs/source/conf.py` and `docs/requirements.txt`) with pre-rendered cache execution (`nb_execution_mode = "off"`).
   - Embedded `[Open in Colab]` badges for instant cloud replication.

## Transition Note: Antigravity CLI / Multi-Agent Workflows
This project supports multi-agent SDD workflows (Antigravity CLI, Gemini CLI, Claude Code, Aider).

**Instruction for the AI Agent**:
1. Read the full tactical history in the `specs/` directory (Phases 001-014).
2. Review the technical manual at [https://spec-craft.readthedocs.io/](https://spec-craft.readthedocs.io/).
3. Use `spec-craft check-env` to verify the local environment.
4. Continue using the SDD workflow (Specify → Plan → Tasks → Implement).
5. Before writing any file to `obsidian/`, run `obsidian help` to detect Obsidian CLI availability.

## Future Roadmap
- Deeper integration with architectural analysis tools (Bonsai/BlenderBIM).
- `obsidian.yaml` command mapping: add `obsidian-bonsai` entry for `trigger_bonsai_build`.
- Extension support for generative music and video.
- Real-time synchronization between Obsidian canvases and tactical tasks.
- SVG driver: handle `<tspan>` nested text replacement without layout breakage.
