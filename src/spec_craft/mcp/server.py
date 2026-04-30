from pathlib import Path
from typing import List, Optional
from fastmcp import FastMCP
from ..core.detector import WorkspaceDetector
from ..core.manager import ConstitutionManager
from ..core.parser import StoryboardParser
from ..core.agent import AgentManager
from ..core.executor import ScriptExecutor
from ..core.build import BuildManager
from ..core.drivers.svg import SVGDriver
from ..core.drivers.cad import CADDriver

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
    build_manager = BuildManager(detector.root_path)
    svg_driver = SVGDriver()
    cad_driver = CADDriver(detector.root_path)
    
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

    @mcp.tool()
    def trigger_svg_build(template_path: str, obsidian_path: str, lang: str) -> str:
        """Generates a translated SVG from a template and Obsidian dictionary.
        
        Args:
            template_path: Path to the SVG template relative to templates/ (e.g., 'scene1.svg').
            obsidian_path: Path to the Obsidian file containing 'translations' relative to obsidian/ (e.g., 'ja/scene1.md').
            lang: Language code for the output directory (e.g., 'ja').
        """
        # Load translations from Obsidian
        storyboard = parser.parse(obsidian_path)
        translations = storyboard.metadata.get("translations", {})
        
        # Resolve paths
        t_path = build_manager.resolve_template_path(template_path)
        output_name = Path(template_path).name
        o_path = build_manager.get_output_path("manga", lang, output_name)
        
        # Execute build
        svg_driver.inject_text(t_path, o_path, translations)
        
        return str(o_path.relative_to(detector.root_path))

    @mcp.tool()
    def trigger_cad_build(jscad_code: str, output_name: str) -> str:
        """Generates an STL file from JSCAD code based on Obsidian requirements.
        
        Args:
            jscad_code: The complete JSCAD source code string.
            output_name: Filename for the generated STL (e.g., 'motor_mount.stl').
        """
        o_path = build_manager.get_output_path("cad", "universal", output_name)
        cad_driver.build_stl(jscad_code, o_path)
        
        return str(o_path.relative_to(detector.root_path))

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

    @mcp.prompt()
    def build_organization_guide() -> str:
        """Explains the hierarchical structure of the build/ directory."""
        return prompts.BUILD_ORGANIZATION_GUIDE

    return mcp

server = create_mcp_server()
