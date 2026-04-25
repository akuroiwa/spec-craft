from fastmcp import FastMCP
from ..core.detector import WorkspaceDetector
from ..core.manager import ConstitutionManager

def create_mcp_server() -> FastMCP:
    """Creates and configures the FastMCP server instance."""
    mcp = FastMCP("spec-craft")
    detector = WorkspaceDetector()
    manager = ConstitutionManager(detector)

    @mcp.tool()
    def analyze_workspace() -> dict:
        """Analyzes the current workspace and returns its structure and metadata."""
        return detector.get_metadata()

    return mcp

server = create_mcp_server()
