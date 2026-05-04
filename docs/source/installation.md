# Installation and Setup

## Prerequisites
Before installing Spec-Craft, ensure you have the following:
- **Python**: Version 3.10 or higher.
- **Node.js**: Required for CAD (JSCAD) builds.
- **uv**: Highly recommended for fast package management.

## Installation
The easiest way to install Spec-Craft is using `uv`:

```bash
git clone https://github.com/akuroiwa/spec-craft.git
cd spec-craft
uv sync
pip install -e .
```

## AI Agent Configuration
Spec-Craft provides an MCP (Model Context Protocol) server. Configuration depends on your AI agent:

### Gemini CLI
Add the following to your `.gemini/settings.json`:

```json
{
  "mcpServers": {
    "spec-craft": {
      "command": "uv",
      "args": ["run", "spec-craft", "serve"]
    }
  }
}
```

### Claude Desktop
Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "spec-craft": {
      "command": "uv",
      "args": ["--directory", "/path/to/spec-craft", "run", "spec-craft", "serve"]
    }
  }
}
```
