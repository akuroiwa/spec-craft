from pathlib import Path
from typing import List, Optional
from fastmcp import FastMCP
from ..core.detector import WorkspaceDetector
from ..core.manager import ConstitutionManager
from ..core.parser import StoryboardParser
from ..core.agent import AgentManager
from ..core.executor import ScriptExecutor

def create_mcp_server(root_path: Optional[Path] = None) -> FastMCP:
    """Creates and configures the FastMCP server instance.
    
    Args:
        root_path: Optional path to the project root. Defaults to CWD.
    """
    mcp = FastMCP("spec-craft")
    detector = WorkspaceDetector(root_path)
    manager = ConstitutionManager(detector)
    
    # Initialize components
    parser = StoryboardParser(detector.root_path / "obsidian")
    agent_manager = AgentManager(detector.root_path)
    executor = ScriptExecutor(detector.root_path)
    
    from . import prompts

    @mcp.tool()
    def analyze_workspace() -> dict:
        """Analyzes the current workspace and returns its structure and metadata."""
        return detector.get_metadata()

    @mcp.tool()
    def read_storyboard(path: str) -> dict:
        """Parses an Obsidian file into a structured structured object.
        
        Args:
            path: Path relative to the obsidian/ directory (e.g., 'storyboard.md').
        """
        storyboard = parser.parse(path)
        return storyboard.model_dump()

    @mcp.tool()
    def check_agent_extensions(required_extensions: List[str]) -> List[dict]:
        """Identifies missing or installed extensions for the agent.
        
        Args:
            required_extensions: List of extension names to check (e.g., ['nano-banana']).
        """
        status = agent_manager.get_extension_status(required_extensions)
        return [info.model_dump() for info in status]

    @mcp.tool()
    def execute_tactical_script(script_name: str, arguments: Optional[List[str]] = None) -> dict:
        """Executes a spec-kit tactical script from .specify/scripts/bash/.
        
        Args:
            script_name: The name of the script file (e.g., 'check-prerequisites.sh').
            arguments: Optional list of command-line arguments for the script.
        """
        return executor.execute(script_name, arguments)

    @mcp.prompt()
    def sdd_strategy_tactics() -> str:
        """Explains the Strategy (Obsidian) vs Tactics (spec-kit) relationship."""
        return prompts.STRATEGY_TACTICS

    @mcp.prompt()
    def manga_storyboard_guide() -> str:
        """Provides guidance for Manga creation within the SDD workflow."""
        return prompts.MANGA_GUIDE

    @mcp.prompt()
    def video_production_guide() -> str:
        """Provides guidance for Video production within the SDD workflow."""
        return prompts.VIDEO_GUIDE

    @mcp.prompt()
    def cad_design_guide() -> str:
        """Provides guidance for CAD modeling (JSCAD) within the SDD workflow."""
        return prompts.CAD_GUIDE

    @mcp.prompt()
    def bootstrap_constitution() -> str:
        """Provides a curated list of SDD rules for new project constitutions."""
        return prompts.BOOTSTRAP_RULES

    @mcp.prompt()
    def agent_extension_guide() -> str:
        """Shows where to install spec-kit extensions for specific AI agents."""
        return prompts.AGENT_EXTENSION_GUIDE_TEMPLATE

    return mcp

server = create_mcp_server()
