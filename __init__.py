# launcher.py
"""
Launcher entrypoint for the GUI. This is the file we will point PyInstaller at
when creating the Windows .exe. It simply starts the GUI.
"""

from ui import run_ui

if __name__ == "__main__":
    run_ui()
