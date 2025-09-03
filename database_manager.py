# database_manager.py
import sqlite3
import os
from pathlib import Path

APP_NAME = "ClipboardManager"

# Choose a per-user data folder:
# - On Windows -> %APPDATA%\ClipboardManager
# - On other OSes -> ~/.clipboardmanager
if os.name == "nt":
    base = Path(os.getenv("APPDATA", Path.home()))
    data_dir = base / APP_NAME
else:
    data_dir = Path.home() / f".{APP_NAME.lower()}"

# Make sure the directory exists
data_dir.mkdir(parents=True, exist_ok=True)

DB_FILE = str(data_dir / "clipboard_history.db")

class DatabaseManager:
    """
    Simple SQLite DB manager for clipboard history.
    DB is created at DB_FILE (per-user folder) so packaged EXEs can write to it.
    """

    def __init__(self):
        # sqlite3 will create the file if it doesn't exist
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_entry(self, content: str):
        query = "INSERT INTO history (content) VALUES (?)"
        self.conn.execute(query, (content,))
        self.conn.commit()

    def get_entries(self, limit=50):
        query = "SELECT id, content, timestamp FROM history ORDER BY id DESC LIMIT ?"
        cur = self.conn.execute(query, (limit,))
        return cur.fetchall()

    def close(self):
        try:
            self.conn.close()
        except Exception:
            pass
