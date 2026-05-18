import subprocess
import os
import time
from pathlib import Path
from typing import Optional, List

class EmacsManager:
    """Manages project-specific Emacs daemon and client interactions."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.sandbox_dir = project_root / ".spec-craft" / "emacs"
        self.socket_name = f"spec_craft_{hash(str(project_root)) % 10000}"

    def ensure_sandbox(self):
        """Creates the Emacs sandbox directory and populates it with init.el if missing."""
        self.sandbox_dir.mkdir(parents=True, exist_ok=True)
        init_el = self.sandbox_dir / "init.el"
        
        if not init_el.is_file():
            template_path = Path(__file__).parent.parent / "data" / "emacs" / "init.el"
            if template_path.is_file():
                init_el.write_text(template_path.read_text())
            else:
                # Fallback minimal init
                init_el.write_text(";; Minimal Spec-Craft Emacs Init\n(require 'server)\n(server-start)\n")

    def start_daemon(self):
        """Starts the Emacs daemon with the project-specific init directory."""
        self.ensure_sandbox()
        
        # Check if already running
        if self.is_daemon_running():
            return True

        command = [
            "emacs",
            "--init-directory", str(self.sandbox_dir),
            f"--daemon={self.socket_name}",
            "--no-window-system"
        ]
        
        try:
            subprocess.run(command, check=True, capture_output=True)
            # Wait a bit for the socket to initialize
            time.sleep(1)
            return True
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to start Emacs daemon: {e.stderr.decode()}")

    def is_daemon_running(self) -> bool:
        """Checks if the specific Emacs daemon is already running."""
        try:
            result = subprocess.run(
                ["emacsclient", f"--socket-name={self.socket_name}", "--eval", "(+ 1 1)"],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def execute_command(self, elisp: str) -> str:
        """Executes an Elisp command via emacsclient."""
        if not self.is_daemon_running():
            self.start_daemon()

        command = [
            "emacsclient",
            f"--socket-name={self.socket_name}",
            "--eval", elisp
        ]
        
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def edit_file(self, file_path: str, elisp_action: str) -> str:
        """Opens a file in the daemon and performs an action."""
        abs_path = os.path.abspath(file_path)
        # Find file, execute action, save
        full_command = f"(with-current-buffer (find-file-noselect \"{abs_path}\") {elisp_action} (save-buffer))"
        return self.execute_command(full_command)

    def stop_daemon(self):
        """Stops the Emacs daemon."""
        return self.execute_command("(kill-emacs)")
