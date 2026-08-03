import re
from pathlib import Path
from typing import Dict, List, Optional
import yaml
from pydantic import BaseModel

class Section(BaseModel):
    """A structured section of a storyboard, representing a header and its content."""
    title: str
    level: int
    content: str

class Storyboard(BaseModel):
    """A complete strategic roadmap parsed from an Obsidian Markdown file."""
    file_path: str
    metadata: Dict
    sections: List[Section]

class StoryboardParser:
    """Parses Obsidian Markdown files into structured Storyboard objects."""

    def __init__(self, obsidian_dir: Path):
        self.obsidian_dir = obsidian_dir

    def parse(self, relative_path: str) -> Storyboard:
        """Parses a file relative to the obsidian directory."""
        file_path = self.obsidian_dir / relative_path
        if not file_path.is_file():
            raise FileNotFoundError(f"Storyboard file not found: {file_path}")

        raw_content = file_path.read_text()
        
        # Parse YAML frontmatter
        metadata = {}
        content = raw_content
        if raw_content.startswith("---"):
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw_content, re.DOTALL)
            if match:
                metadata = yaml.safe_load(match.group(1)) or {}
                content = raw_content[match.end():]

        # Temporarily replace fenced code blocks to avoid parsing headers inside them
        code_blocks = []
        def repl(m):
            code_blocks.append(m.group(0))
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"
        
        code_fence_regex = re.compile(r"```.*?```", re.DOTALL)
        content_replaced = code_fence_regex.sub(repl, content)

        # Parse Sections
        sections = []
        header_regex = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
        
        # Split content by headers
        parts = header_regex.split(content_replaced)
        
        # Helper to restore code blocks in strings
        def restore_blocks(text: str) -> str:
            for idx, block in enumerate(code_blocks):
                text = text.replace(f"__CODE_BLOCK_{idx}__", block)
            return text

        # parts[0] is the preamble before the first header
        if parts[0].strip():
            sections.append(Section(
                title="Preamble",
                level=0,
                content=restore_blocks(parts[0].strip())
            ))
            
        for i in range(1, len(parts), 3):
            level = len(parts[i])
            title = restore_blocks(parts[i+1].strip())
            body = restore_blocks(parts[i+2].strip())
            sections.append(Section(title=title, level=level, content=body))

        return Storyboard(
            file_path=str(file_path),
            metadata=metadata,
            sections=sections
        )

