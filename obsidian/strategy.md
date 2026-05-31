# Spec-Craft Strategic Roadmap

## Core Philosophy
Spec-Craft is built on **Spec-Driven Development (SDD)**. 
- **Strategy (Obsidian)**: Defines the "What" and "Why". It is the project's soul.
- **Tactics (spec-kit)**: Defines the "How". It handles iterative implementation cycles.

## Current Milestone: v0.1.2 Reached
The foundation of Spec-Craft is complete.
- Multi-domain generation: 2D (SVG), 3D (Blender/Bonkei), CAD (JSCAD), BIM (Bonsai).
- Visual Feedback: AI can "see" assets via SVG projections.
- Isolated Editing: AI-dedicated Emacs sandbox with LSP/Linting.
- Transparency: "Suggest-and-Confirm" workflow for secure operations.

## Transition Note: From gemini-cli to Antigravity CLI / Multi-Agent Workflows
This project is transitioning to a new AI agent environment (Antigravity CLI) and now supports general multi-agent SDD workflows (including Antigravity CLI, Gemini CLI, Claude Code, and Aider).
**Instruction for the AI Agent**:
1. Read the full tactical history in the `specs/` directory (Phases 001-013).
2. Review the technical manual at [https://spec-craft.readthedocs.io/](https://spec-craft.readthedocs.io/).
3. Use `spec-craft check-env` to verify the local environment.
4. Continue using the SDD workflow (Specify -> Plan -> Tasks -> Implement).
5. For Aider or local workflows, utilize direct markdown skill reading or `spec-kit-mcp` integration options.

## Future Roadmap
- Deeper integration with architectural analysis tools.
- Extension support for generative music and video.
- Real-time synchronization between Obsidian canvases and tactical tasks.
