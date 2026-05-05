# Spec-Craft

Obsidian-based Spec-Driven Development (SDD) toolkit with MCP and spec-kit integration.

## Concept

`spec-craft` is a bridge between high-level roadmaps in Obsidian and tactical implementation using `spec-kit`.

### Strategy vs Tactics
- **Strategy (Obsidian)**: Defines the "What" and "Why". It holds the project's soul, long-term roadmap, and domain-specific principles (Manga storyboards, CAD logic, Blender Bonkei rules, etc.).
- **Tactics (spec-kit)**: Defines the "How". It executes iterative SDD cycles (Specify → Plan → Implement) to generate concrete code and assets based on the strategy.

## Installation

```bash
uv sync
pip install -e .
```

### spec-kit Extension Setup
To enable slash commands (e.g., `/speckit.obsidian-analyze`), copy the `extension/` folder to your project's `.specify/extensions/spec-craft/` directory.

## Usage

### Build Output Organization
All generated assets are stored in the `build/` directory:
- `build/manga/<lang>/`: Translated SVG scenes.
- `build/cad/universal/`: Parametric STL models and SVG projections.
- `build/3d/universal/`: Blender Python scripts for scene construction.

### 3D Preview
To view your generated CAD models interactively, run:
```bash
spec-craft browse
```
This starts a local server and opens a Three.js viewer. You can load specific models using query parameters: `http://localhost:8080/?model=cad/universal/my_part.stl`.

### Visual Feedback Loop
When triggering a CAD build, spec-craft can generate SVG projections of the model. These are ideal for AI vision analysis, allowing your agent to "see" the dimensions and propose improvements.

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
