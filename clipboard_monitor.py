import pyperclip
import time
from database_manager import DatabaseManager

class ClipboardMonitor:
    def __init__(self, interval=1):
        self.interval = interval
        self.last_text = ""
        self.db = DatabaseManager()

    def start(self):
        print("Clipboard monitor started... Press Ctrl+C to stop.")
        while True:
            try:
                text = pyperclip.paste()
                if text and text != self.last_text:
                    self.db.add_entry(text)
                    print(f"Captured: {text[:40]}...")  # preview only
                    self.last_text = text
                time.sleep(self.interval)
            except KeyboardInterrupt:
                print("Stopped monitoring clipboard.")
                break
