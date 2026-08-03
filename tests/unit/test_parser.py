import pytest
from pathlib import Path
from spec_craft.core.parser import StoryboardParser, Storyboard

def test_parse_simple_storyboard(temp_workspace):
    """Verify parsing of a basic markdown file with frontmatter and headers."""
    obsidian_dir = temp_workspace / "obsidian"
    obsidian_dir.mkdir(parents=True, exist_ok=True)
    
    file_content = """---
title: My Strategy
tags: [test, sdd]
---
# Character: Hero
Content about the hero.

## Background
More details.

# Setting: Castle
Dark and gloomy.
"""
    story_file = obsidian_dir / "strategy.md"
    story_file.write_text(file_content)
    
    parser = StoryboardParser(obsidian_dir)
    storyboard = parser.parse("strategy.md")
    
    assert storyboard.metadata["title"] == "My Strategy"
    assert "sdd" in storyboard.metadata["tags"]
    
    assert len(storyboard.sections) == 3
    assert storyboard.sections[0].title == "Character: Hero"
    assert storyboard.sections[0].level == 1
    assert "Content about the hero." in storyboard.sections[0].content
    
    assert storyboard.sections[1].title == "Background"
    assert storyboard.sections[1].level == 2
    
    assert storyboard.sections[2].title == "Setting: Castle"

def test_parse_missing_file(temp_workspace):
    """Verify behavior when file is missing."""
    parser = StoryboardParser(temp_workspace)
    with pytest.raises(FileNotFoundError):
        parser.parse("ghost.md")

def test_parse_fenced_code_blocks(temp_workspace):
    """Verify that headers and comments inside fenced code blocks are not split into sections."""
    obsidian_dir = temp_workspace / "obsidian"
    obsidian_dir.mkdir(parents=True, exist_ok=True)
    
    file_content = """---
title: Fenced Test
---
# Actual Heading

Some preamble text.

```python
# This is a comment, not a heading!
## Still a comment
def test():
    pass
```

## Another Heading

More content.
"""
    story_file = obsidian_dir / "fenced_test.md"
    story_file.write_text(file_content)
    
    parser = StoryboardParser(obsidian_dir)
    storyboard = parser.parse("fenced_test.md")
    
    # We expect exactly 2 sections: "Actual Heading" and "Another Heading".
    # Preamble should not be created if empty, but "Some preamble text. ..." is the content of "Actual Heading".
    # Wait, the heading "Actual Heading" is level 1, so:
    # sections[0] -> title="Actual Heading", content contains "Some preamble text." and the code block.
    # sections[1] -> title="Another Heading", content contains "More content."
    assert len(storyboard.sections) == 2
    assert storyboard.sections[0].title == "Actual Heading"
    assert "This is a comment, not a heading!" in storyboard.sections[0].content
    assert "Still a comment" in storyboard.sections[0].content
    assert storyboard.sections[1].title == "Another Heading"

