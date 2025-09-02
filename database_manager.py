import sqlite3
import os

DB_FILE = "clipboard_history.db"

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
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
        return self.conn.execute(query, (limit,)).fetchall()
