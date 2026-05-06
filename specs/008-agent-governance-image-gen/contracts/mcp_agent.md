# MCP Contract: Agent Governance & Generative Flows

## Tools

### `check_generative_capabilities`
- **Purpose**: Verify if the required tools for a creative domain are installed.
- **Input**: `domain` (String: "manga", "music", "video", "cad")
- **Output**: JSON containing `has_capability` and `missing_extensions` (List of objects with name and install_command).

## Prompts

### `generative-workflow-guide`
- **Role**: Explains the step-by-step process of going from an Obsidian strategy to an implemented creative asset.

### `agent-extension-guide` (Updated)
- **Role**: Provides the registry URL and tailored installation paths.
- **Includes**: Links to `https://geminicli.com/extensions/`.
