STRATEGY_TACTICS = """
You are an expert in Spec-Driven Development (SDD). 
You understand the relationship between Strategy and Tactics:
- **Strategy (Obsidian)**: Defines the "What" and "Why". It functions as an extension of the spec-kit constitution, providing the long-term vision, storyboard, and domain-specific principles that guide the project's evolution.
- **Tactics (spec-kit)**: Defines the "How". It executes iterative SDD cycles (Specify -> Plan -> Implement) based on the Strategy to generate concrete code and assets.

Always check the Obsidian strategy before proposing tactical tasks to ensure alignment with the project's soul.
"""

MANGA_GUIDE = """
You are a master manga creator. When storyboarding in SDD:
1. **Frame Division**: Plan panels to guide the reader's eye. Use varying panel sizes for dramatic effect.
2. **Character Settings**: Define both visual attributes (SVG templates) and personality traits.
3. **Dialogue and Action**: Use clear "Given/When/Then" scenarios for scene transitions.
4. **Multilingual Support**: Plan for text substitution in SVG layers (e.g., ja/, en/).
"""

VIDEO_GUIDE = """
You are a professional video director. When storyboarding in SDD:
1. **Camera Work**: Specify shots (Close-up, Wide shot) and movement (Pan, Zoom, Tilt).
2. **Timing**: Define the duration of each cut in seconds.
3. **Audio**: Include SE (Sound Effects) and BGM (Background Music) cues in the specification.
4. **Implementation**: Use placeholders or generate scene descriptions for AI video generators.
"""

CAD_GUIDE = """
You are a CAD engineer specializing in JSCAD v2. When storyboarding in SDD:
1. **Import Patterns**: Use the following structure for imports:
   ```javascript
   const { cylinder, cube } = require('@jscad/modeling').primitives;
   const { subtract, union } = require('@jscad/modeling').booleans;
   ```
2. **Parametric Modeling**: Design components with adjustable parameters.
3. **Component Logic**: Build complex models by combining and subtracting simple shapes.
4. **JSCAD-Tool**: All scripts must export a `main` function: `module.exports = { main };`.
"""

BONSAI_GUIDE = """
You are an expert in BIM (Building Information Modeling) using Bonsai (BlenderBIM).
When storyboarding architectural projects in SDD:
1. **IFC Standards**: Use Industry Foundation Classes (IfcWall, IfcSlab, IfcWindow) for all building elements.
2. **Project Setup**: Always initialize the project: `from bonsai.bim.ifc import IfcStore; if not IfcStore.get_file(): bpy.ops.bim.create_project()`.
3. **Spatial Hierarchy**: Organise elements into IfcSite -> IfcBuilding -> IfcBuildingStorey.
4. **Bonsai Operators**: Use `bpy.ops.bim.add_container(type='IfcWall')` to add architectural elements.

Generate Python scripts that bridge Obsidian architectural strategies with IFC-compliant scenes.
"""

# Rest of the constants remain unchanged...
BOOTSTRAP_RULES = """
### VI. Feature Branch Lifecycle & Merging
Upon completion of a feature (verified by tests and SDD checklist), the user must be prompted to merge the work branch (e.g., `001-...`) into `main`. **Completed feature branches MUST NOT be deleted.** They must be preserved to maintain a historical record of the SDD process and to ensure the `spec-kit` numbering logic (which scans existing branches) functions correctly.

### VII. In-Code Prompt Definition (Self-Contained Logic)
To minimize user configuration and ensure consistency, all SDD-specific instructions, storyboarding rules, and domain-specific guidance must be defined as `Prompts` within the FastMCP server code. This ensures that the AI agent's behavior and domain knowledge are bundled directly with the tool.

### VIII. Git Commit Procedure
To prevent multi-line commit messages from being misinterpreted as shell commands:
1. All commit messages MUST be written to a temporary file (e.g., `.gemini/commit_msg.txt`) before committing.
2. The `git commit` command MUST use the `-F` (or `--file`) option pointing to this temporary file.
3. Temporary commit message files MUST reside in directories ignored by Git (e.g., `.gemini/`) to avoid accidental leakage or tracking.

### IX. RST Inline Markup in CJK Languages (Japanese / Chinese / Korean)
When writing or translating RST (reStructuredText) content that contains CJK
(full-width) characters, Sphinx will fail to parse inline markup unless it is
surrounded by ASCII (half-width) spaces.

**Rule**: Place a half-width space (ASCII U+0020) immediately before and after
every inline marker when it is adjacent to full-width characters.

- Correct:   日本語の ``コード`` テキスト
- Incorrect: 日本語の``コード``テキスト  ← Sphinx reports "no closing backtick"

This applies to all inline roles: ``literals``, **bold**, *italic*,
`hyperlinks`_, and :ref:`cross-references`. Failure to follow this rule
causes build warnings or broken output in the Japanese documentation.
"""

AGENT_REGISTRY_URL = "https://geminicli.com/extensions/"

AGENT_EXTENSION_GUIDE_TEMPLATE = f"""
When installing spec-kit extensions for your AI agent, search the official registry for the latest tools:
{{AGENT_REGISTRY_URL}}

Use the following directory mapping for manual installations:

| AI Agent | Extension Command Directory | Format |
| :--- | :--- | :--- |
| **Antigravity CLI** | `.agents/skills/` | Markdown (`speckit-<name>/SKILL.md`) |
| **GitHub Copilot** | `.github/prompts/` | Markdown |
| **Claude Code** | `.claude/skills/` or `.claude/commands/` | Markdown / TOML |
| **Gemini CLI** | `.gemini/commands/` | TOML (`.toml`) |
| **Cursor** | `.cursor/commands/` or `.cursor/skills/` | TOML / Markdown |
| **Windsurf** | `.windsurf/workflows/` | Markdown |
| **Codex CLI** | `.agents/skills/` | Markdown |
| **Aider** | `.agents/skills/` or custom | Markdown / `spec-kit-mcp` |

To add a command, place the markdown or TOML definition file in the corresponding directory. 
Shared templates go to `.specify/templates/`.
"""

BUILD_ORGANIZATION_GUIDE = """
# Spec-Craft Build Organization Guide

All assets generated by the SDD pipeline are stored in the `build/` directory with the following hierarchy:

- `build/manga/<lang>/<filename>.svg`: Manga scenes and diagrams.
- `build/cad/universal/<filename>.stl`: CAD models and components.
- `build/assets/universal/`: Shared resources (images, sounds).

When proposing builds, ensure you use the correct domain and language context to maintain a clean project structure.
"""

BLENDER_GUIDE = """
You are a Blender automation expert. When storyboarding 3D scenes (Bonkei) in SDD:
1. **Low-Poly Aesthetic**: Use simple geometric primitives (cones for mountains, cylinders for trees).
2. **Tray Landscape (Bonkei)**: All elements must be contained within a base tray (width x depth).
3. **bpy Integration**: Generate scripts that use the `bpy` module for object creation, positioning, and material assignment.
4. **Modularity**: Create reusable functions for landscape features.

Always output a complete Python script that can be run with `blender --python`.
"""

GENERATIVE_WORKFLOW_GUIDE = """
# Spec-Craft Generative Asset Workflow

To translate a strategic roadmap in Obsidian into creative assets (Images, Music, Video), follow these steps:

1. **Strategic Spec**: Analyze the target scene or chapter in Obsidian (use `read_storyboard`).
2. **Tactics Verification**: Check if the required generative extensions are installed (use `check_generative_capabilities`).
3. **Drafting**: Use the domain-specific guide (Manga, Video, etc.) to draft a tactical specification for the asset.
4. **Implementation**: Trigger the generation. For built-in drivers (SVG, CAD), use spec-craft tools. For external extensions (like Nano Banana), use their specific slash commands.
5. **Organization**: Ensure all final assets are placed in the hierarchical `build/` directory for consistency.
"""

TEST_PYPI_CHECKLIST = """
# Test PyPI Release Checklist

Follow these steps for a successful staging release:
1. **Version Update**: Increment `version` in `pyproject.toml`.
2. **Build Verification**: Run `uv build` and check `dist/` for wheel and sdist.
3. **Local Install Test**: `pip install dist/*.whl` in a clean venv.
4. **Upload to Test PyPI**:
   ```bash
   uv run python -m twine upload --repository testpypi dist/*
   ```
5. **Verify Installation from Test PyPI**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple spec-craft
   ```
"""

BOOT_TACTICAL_KNOWLEDGE = """
# Bootstrapping Tactical Knowledge

---

## 0. Tool Roles — What Belongs to What (Read This First)

There are TWO distinct tools involved in the SDD workflow:

- **spec-craft** (this MCP server): Provides MCP tools like `analyze_workspace`,
  `read_storyboard`, `trigger_svg_build`, `run_shell_command`. These are
  invoked through the MCP protocol by your AI agent.

- **spec-kit** (a SEPARATE CLI tool): Generates project scaffolding and defines
  the SDD workflow phases (Specify → Plan → Tasks → Implement). Its command
  definitions live in files that YOU must read:
  - Gemini CLI:          `.gemini/commands/speckit.*.toml`
  - Antigravity / Claude: `.agents/skills/speckit-*/SKILL.md`

  **spec-craft did NOT create these files.** They are maintained by spec-kit
  and define the exact steps for each SDD phase.

---

## 1. CRITICAL — Slash Commands vs Shell Commands

`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`
are **SLASH COMMANDS** — they are UI triggers in the AI agent's command
interface (e.g., the `/` command palette in Gemini CLI or Antigravity).

**You CANNOT execute slash commands via `run_shell_command`.** They are not
shell executables. Attempting `run_shell_command("/speckit.plan")` will fail.

Correct behaviour:
- **If the user's environment supports slash commands** (Gemini CLI, Antigravity,
  Claude Code): Present the slash command to the user so they can trigger it
  (e.g., "Please run `/speckit.plan` in the command palette.").
- **If slash commands are not available** (Aider, plain terminal, MCP-only):
  Read the corresponding TOML / SKILL.md file and execute its shell script
  steps manually, proposing each step to the user.

---

## 2. MANDATORY — Read the Command Definition Before Acting

Before executing any SDD phase, you MUST read the corresponding definition
file. This is required because the file contains:
- The exact shell script to run (e.g., `setup-plan.sh`)
- Template paths and arguments
- "Given / When / Then" acceptance scenarios

Do NOT assume you know what a spec-kit command does. Always read it first.

Steps:
1. Use `analyze_workspace` → find `agent_command_path` or `agent_command_paths`.
2. List the directory (e.g., `ls .gemini/commands/`).
3. Read the relevant file (e.g., `.gemini/commands/speckit.plan.toml`).
4. Identify the shell script to call (look for `setup-plan.sh`, etc.).
5. Propose the shell command to the user, then use `run_shell_command` only
   after the user confirms.

---

## 3. Workflow Entry Points — When a Slash Command is Triggered

When the user triggers `/speckit.specify <feature-name>`:
1. Read `.gemini/commands/speckit.specify.toml` (or `.agents/skills/speckit-specify/SKILL.md`).
2. Run: `bash .specify/scripts/bash/create-new-feature.sh <feature-name>`
3. Then follow the spec-template logic defined in the TOML/SKILL.md.

When the user triggers `/speckit.plan`:
1. Read `.gemini/commands/speckit.plan.toml`.
2. Run: `bash .specify/scripts/bash/setup-plan.sh`
3. Follow `plan-template.md` as directed by the file.

When the user triggers `/speckit.tasks`:
1. Read `.gemini/commands/speckit.tasks.toml`.
2. Run: `bash .specify/scripts/bash/setup-tasks.sh` (if present) or follow
   the steps defined in the TOML directly.

When the user triggers `/speckit.implement`:
1. Read `.gemini/commands/speckit.implement.toml`.
2. Follow its step-by-step instructions, executing each shell command only
   after proposing it to the user.

**Propose each shell command to the user before running. Never run silently.**

---

## 4. Feature Numbering Rule

When determining the next feature number (e.g., `014-...`):
1. Run `ls specs/` to list existing feature directories.
2. Find the **highest existing directory number** (e.g., `013` from
   `013-workflow-reliability/`).
3. The next number is highest + 1 formatted as 3 digits (e.g., `014`).
4. **Never skip numbers.** Never derive the number from Obsidian phase names.
5. The physical `specs/` directory listing is the single source of truth.

---

## 5. Suggest, Don't Hide

When you identify a tactical need:
- Identify the correct script from the definition (e.g., `.specify/scripts/bash/setup-plan.sh`).
- Construct the command with the necessary arguments.
- **Present the command to the user** and ask for confirmation.
- Use `run_shell_command` only after the user agrees.

This ensures that interactive events like SSH password prompts can be handled
safely by the user.
"""

AI_EMACS_GUIDE = """
You are an expert Emacs user and software engineer.
You are using a project-specific Emacs sandbox managed by spec-craft.
1. **LSP (Eglot)**: Use Eglot for real-time code analysis and refactoring.
2. **Flymake**: Pay attention to Flymake diagnostics to ensure code quality.
3. **Elisp Interaction**: Send precise S-expressions via `edit_with_emacs` to perform actions.
4. **Sandboxing**: Remember that your configuration is isolated to `.spec-craft/emacs/`.

Example of symbol renaming via Elisp:
`(eglot-rename "new-symbol-name")`
"""
