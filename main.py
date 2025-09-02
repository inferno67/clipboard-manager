import argparse
from clipboard_monitor import ClipboardMonitor
from ui import run_ui

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ui", action="store_true", help="Run with UI")
    args = parser.parse_args()

    if args.ui:
        run_ui()
    else:
        monitor = ClipboardMonitor()
        monitor.start()
