# Data Model: Agent Capabilities & Workflows

## Entities

### GenerativeCapability
A specific creative action the agent can perform.
- `intent_id`: String (e.g., "manga_illustration", "sdd_cad")
- `required_extension`: String (e.g., "nano-banana")
- `command_signature`: String (e.g., "nanobanana.gen")
- `category`: Enum (IMAGE, AUDIO, VIDEO, CAD, 3D)

### AgentRegistry
The official source for discovering new tools.
- `url`: String ("https://geminicli.com/extensions/")
- `last_checked`: DateTime

### ProductionTask
A tactical execution unit in a creative domain.
- `source_spec`: Path (to Obsidian file)
- `target_domain`: String
- `language`: String
- `build_status`: String

## Relationships
- `spec-craft` checks for `GenerativeCapability` before starting a `ProductionTask`.
- `agent_extension_guide` references the `AgentRegistry`.
