# Spec-Craft

Obsidian-based Spec-Driven Development (SDD) toolkit with MCP and spec-kit integration.

## Concept

`spec-craft` is a bridge between high-level roadmaps in Obsidian and tactical implementation using `spec-kit`.

### Strategy vs Tactics
- **Strategy (Obsidian)**: Defines the "What" and "Why". It holds the project's soul, long-term roadmap, and domain-specific principles (Manga storyboards, CAD logic, etc.).
- **Tactics (spec-kit)**: Defines the "How". It executes iterative SDD cycles (Specify → Plan → Implement) to generate concrete code and assets based on the strategy.

## Installation

```bash
pip install -e .
```

## Usage

### CLI

```bash
spec-craft --version
spec-craft serve
```

### MCP Server

Register the server in your MCP client (e.g., Claude Desktop, Gemini CLI) using:

```json
{
  "mcpServers": {
    "spec-craft": {
      "command": "spec-craft",
      "args": ["serve"]
    }
  }
}
```
