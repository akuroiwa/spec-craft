from pathlib import Path
from typing import List, Optional
from fastmcp import FastMCP
from spec_craft.core.detector import WorkspaceDetector
from spec_craft.core.manager import ConstitutionManager
from spec_craft.core.parser import StoryboardParser
from spec_craft.core.agent import AgentManager, GenerativeDomain
from spec_craft.core.executor import ScriptExecutor
from spec_craft.core.build import BuildManager
from spec_craft.core.drivers.svg import SVGDriver
from spec_craft.core.drivers.cad import CADDriver
from spec_craft.core.drivers.blender import BlenderDriver
from spec_craft.mcp import prompts

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
    blender_driver = BlenderDriver(detector.root_path)
    from spec_craft.core.drivers.bonsai import BonsaiDriver
    bonsai_driver = BonsaiDriver(detector.root_path)

    @mcp.tool()
    def analyze_workspace() -> dict:
        """Analyzes the current workspace and returns its structure and metadata."""
        return detector.get_metadata()

    @mcp.tool()
    def check_environment() -> List[dict]:
        """Detects missing prerequisites for the full Spec-Craft pipeline."""
        return detector.check_environment()

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
    def check_generative_capabilities(domain: str) -> dict:
        """Verifies if the required tools for a creative domain are available.
        
        Args:
            domain: The creative domain (e.g., 'manga', 'music', 'video', 'cad', '3d').
        """
        try:
            gen_domain = GenerativeDomain(domain.lower())
            capability = agent_manager.check_generative_capabilities(gen_domain)
            return capability.model_dump()
        except ValueError:
            return {"error": f"Invalid domain: {domain}. Supported domains are: {[d.value for d in GenerativeDomain]}"}

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
    def trigger_cad_build(jscad_code: str, output_name: str, formats: Optional[List[str]] = None) -> dict:
        """Generates CAD files (STL, SVG) from JSCAD code based on Obsidian requirements.
        
        Args:
            jscad_code: The complete JSCAD source code string.
            output_name: Filename for the generated assets (e.g., 'motor_mount'). Extension added automatically.
            formats: Optional list of formats to generate (default: ['stl', 'svg']).
        """
        requested_formats = formats or ["stl", "svg"]
        o_base = build_manager.get_output_path("cad", "universal", output_name)
        
        results = cad_driver.build(jscad_code, o_base, requested_formats)
        
        return {
            fmt: str(path.relative_to(detector.root_path)) 
            for fmt, path in results.items()
        }

    @mcp.tool()
    def generate_blender_script(scene_spec: dict, output_name: str) -> str:
        """Generates a Blender Python script for scene construction.
        
        Args:
            scene_spec: A dictionary describing the Bonkei scene (width, depth, elements).
            output_name: Filename for the script (e.g., 'bonkei.py').
        """
        o_path = build_manager.get_output_path("3d", "universal", output_name)
        blender_driver.generate_script(scene_spec, o_path)
        
        return str(o_path.relative_to(detector.root_path))

    @mcp.tool()
    def trigger_full_build() -> dict:
        """Coordinates a full build of all pending assets (SVG, CAD, 3D, Architecture)."""
        return {
            "status": "Ready",
            "capabilities": ["manga (svg)", "cad (stl)", "3d (blender-py)", "architecture (ifc-py)"],
            "message": "Full build orchestration initialized. Use domain triggers for generation."
        }

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
        return prompts.AGENT_EXTENSION_GUIDE_TEMPLATE.format(AGENT_REGISTRY_URL=prompts.AGENT_REGISTRY_URL)

    @mcp.prompt()
    def generative_workflow_guide() -> str:
        """Explains the Strategic -> Tactics -> Implementation workflow for creative assets."""
        return prompts.GENERATIVE_WORKFLOW_GUIDE

    @mcp.prompt()
    def build_organization_guide() -> str:
        """Explains the hierarchical structure of the build/ directory."""
        return prompts.BUILD_ORGANIZATION_GUIDE

    @mcp.prompt()
    def blender_3d_guide() -> str:
        """Provides guidance for 3D scene construction (Bonkei) in Blender."""
        return prompts.BLENDER_GUIDE

    @mcp.prompt()
    def bonsai_architectural_guide() -> str:
        """Provides guidance for IFC-compliant modeling in Blender (Bonsai)."""
        return prompts.BONSAI_GUIDE

    @mcp.prompt()
    def test_pypi_release_checklist() -> str:
        """A step-by-step guide for performing the first release to Test PyPI."""
        return prompts.TEST_PYPI_CHECKLIST

    return mcp

if __name__ == "__main__":
    mcp = create_mcp_server()
    mcp.run()
