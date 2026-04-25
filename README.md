# Spec-Craft

Obsidian-based Spec-Driven Development (SDD) toolkit with MCP and spec-kit integration.

## Concept

`spec-craft` is a bridge between high-level roadmaps in Obsidian and tactical implementation using `spec-kit`. It provides an MCP (Model Context Protocol) server to help LLMs understand the project's "soul" and "evolution".

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
