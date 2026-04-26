# Spec-Craft Constitution

## Core Principles

### I. Spec-Driven Development with Obsidian
Every feature begins with a roadmap or storyboard in Obsidian. The Obsidian vault acts as the "soul" of the project, providing a long-term roadmap that guides individual SDD cycles.

### II. Integrated SDD Lifecycle
We use `spec-kit` for tactical implementation. Every code change or asset generation must be preceded by a specification (`/speckit.specify`) and a plan (`/speckit.plan`).
### III. Test-First Implementation
Tests or validation logic must be defined in the plan phase and executed immediately after implementation. No feature is complete without verified behavioral correctness.

### V. Package Management with uv
We use `uv` for all Python package management, including dependency installation, environment management, and script execution. Standard `pip` should be avoided in favor of `uv sync` and `uv run`.

### VI. Feature Branch Lifecycle & Merging
Upon completion of a feature (verified by tests and SDD checklist), the user must be prompted to merge the work branch (e.g., `001-...`) into `main`. The AI must explicitly warn the user if unmerged branches exist before starting a new `specify` cycle to prevent configuration drift.

### VII. In-Code Prompt Definition (Self-Contained Logic)
To minimize user configuration and ensure consistency, all SDD-specific instructions, storyboarding rules, and domain-specific guidance must be defined as `Prompts` within the FastMCP server code. This ensures that the AI agent's behavior and domain knowledge are bundled directly with the tool.

## Development Workflow

### IV. Cross-Domain Generative SDD
The SDD process applies not only to code but also to image, music, and video generation. Specifications must define the "what" and "why" of the creative intent.

## Development Workflow

### Git Commit Procedure
To prevent multi-line commit messages from being misinterpreted as shell commands:
1. All commit messages MUST be written to a temporary file (e.g., `.gemini/commit_msg.txt`) before committing.
2. The `git commit` command MUST use the `-F` (or `--file`) option pointing to this temporary file.
3. Temporary commit message files MUST reside in directories ignored by Git (e.g., `.gemini/`) to avoid accidental leakage or tracking.

## Governance
This Constitution supersedes all other practices. Any divergence from these principles must be justified and documented in the roadmap.

**Version**: 1.0.0 | **Ratified**: 2026-04-25 | **Last Amended**: 2026-04-25
