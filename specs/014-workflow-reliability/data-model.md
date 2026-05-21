# Data Model: Tactical Refinement

## Entities

### TacticalKnowledge
The AI's understanding of how to perform a task.
- `command_name`: String (e.g., "specify")
- `toml_path`: Path
- `logic`: String (parsed from TOML prompt)

### AgentConfig
Metadata about the active AI agent.
- `agent_id`: String ("gemini-cli")
- `command_dir`: Path (".gemini/commands/")

## Relationships
- `analyze_workspace` provides the `AgentConfig`.
- AI reads TOML files from `AgentConfig.command_dir` to build `TacticalKnowledge`.
