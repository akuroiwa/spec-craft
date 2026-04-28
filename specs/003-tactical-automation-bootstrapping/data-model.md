# Data Model: Tactical Automation & Agent Support

## Entities

### TacticalScript
A spec-kit automation script.
- `name`: String (e.g., "setup-plan.sh")
- `path`: Path (Absolute path)
- `args`: List of strings (Command line arguments)

### BootstrapRule
A high-quality SDD guideline.
- `id`: String (e.g., "git-commit-procedure")
- `title`: String
- `content`: String (Markdown formatted rule)

### AgentProfile
Metadata about an AI agent.
- `agent_id`: String (e.g., "claude-code")
- `display_name`: String
- `extension_dir`: String (Relative to project root or absolute)
- `install_command_template`: String

## Relationships
- `spec-craft` executes multiple `TacticalScript`s.
- `spec-craft` suggests a set of `BootstrapRule`s during setup.
- `spec-craft` uses `AgentProfile` to tailor instructions.
