import http.server
import socketserver
import webbrowser
import os
import threading
from pathlib import Path
from typing import Optional
from importlib import resources

class PreviewRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve bundled assets and project build files."""

    def __init__(self, *args, project_root: Path = None, **kwargs):
        self.project_root = project_root
        super().__init__(*args, **kwargs)

    def translate_path(self, path: str) -> str:
        """Maps URLs to either package resources or the project build directory."""
        # Clean path
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]

        # 1. Serve index.html and viewer.js from package static resources
        if path in ["/", "/index.html", "/viewer.js"]:
            resource_name = "index.html" if path in ["/", "/index.html"] else "viewer.js"
            try:
                # Get the path to the bundled resource
                p = resources.files("spec_craft.static").joinpath(resource_name)
                if p.is_file():
                    return str(p)
                raise FileNotFoundError()
            except (ModuleNotFoundError, AttributeError, FileNotFoundError):
                # Fallback for development if not installed as package
                dev_path = self.project_root / "src" / "spec_craft" / "static" / resource_name
                return str(dev_path)

        # 2. Serve files from the project's build/ directory at /build/
        if path.startswith("/build/"):
            relative_path = path[len("/build/"):]
            # Prevent directory traversal
            if ".." in relative_path:
                return ""
            return str(self.project_root / "build" / relative_path)

        return super().translate_path(path)

class PreviewServer:
    """Manages the local HTTP server for 3D previewing."""

    def __init__(self, project_root: Path, port: int = 8080):
        self.project_root = project_root
        self.port = port
        self.httpd: Optional[socketserver.TCPServer] = None
        self._thread: Optional[threading.Thread] = None

    def start(self, open_browser: bool = True):
        """Starts the server in a background thread."""
        handler = lambda *args, **kwargs: PreviewRequestHandler(
            *args, project_root=self.project_root, **kwargs
        )
        
        # Use allow_reuse_address to avoid "Address already in use" errors
        socketserver.TCPServer.allow_reuse_address = True
        self.httpd = socketserver.TCPServer(("", self.port), handler)
        
        print(f"Spec-Craft Preview Server started at http://localhost:{self.port}")
        
        self._thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self._thread.start()

        if open_browser:
            webbrowser.open(f"http://localhost:{self.port}")

    def stop(self):
        """Stops the server."""
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
