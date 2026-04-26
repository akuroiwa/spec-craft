# MCP Contract: Obsidian Hub & Agent Management

## Tools

### `read_storyboard`
- **Purpose**: Parse an Obsidian file into a structured JSON object.
- **Input**: `path` (relative to `obsidian/` directory)
- **Output**: `Storyboard` entity JSON.

### `check_agent_extensions`
- **Purpose**: Identify missing or installed extensions.
- **Input**: `required_extensions` (List of strings)
- **Output**: List of `ExtensionInfo` objects.

## Prompts

### `sdd-strategy-tactics`
- **Role**: Explains the Obsidian (Strategy) vs spec-kit (Tactics) philosophy.

### `manga-storyboard-guide`
- **Role**: Provides rules for frame division and character consistency.

### `video-production-guide`
- **Role**: Provides rules for camera work and cut timing.

### `cad-design-guide`
- **Role**: Provides rules for parametric JSCAD modeling.
