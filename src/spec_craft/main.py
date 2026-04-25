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
    
    args = parser.parse_args()
    
    if args.command == "serve":
        print("Starting spec-craft MCP server...")
        server.run()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
