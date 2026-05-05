import argparse
import sys
from spec_craft import __version__
from spec_craft.mcp.server import server

def main():
    parser = argparse.ArgumentParser(description="spec-craft: Obsidian-based SDD toolkit")
    parser.add_argument("--version", action="version", version=f"spec-craft {__version__}")
    
    subparsers = parser.add_subparsers(dest="command")
    
    # serve command
    subparsers.add_parser("serve", help="Start the MCP server")

    # browse command
    browse_parser = subparsers.add_parser("browse", help="Start the local 3D preview server")
    browse_parser.add_argument("--port", type=int, default=8080, help="Port to run the server on")
    browse_parser.add_argument("--no-browser", action="store_true", help="Don't open the system browser automatically")
    
    args = parser.parse_args()
    
    if args.command == "serve":
        print("Starting spec-craft MCP server...")
        server.run()
    elif args.command == "browse":
        from spec_craft.core.detector import WorkspaceDetector
        from spec_craft.core.ui.server import PreviewServer
        
        detector = WorkspaceDetector()
        ui_server = PreviewServer(detector.root_path, port=args.port)
        ui_server.start(open_browser=not args.no_browser)
        
        try:
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping preview server...")
            ui_server.stop()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
