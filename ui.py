from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton # type: ignore
import sys
from database_manager import DatabaseManager
import pyperclip # type: ignore

class ClipboardUI(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setWindowTitle("Clipboard Manager")
        self.resize(500, 400)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.refresh_button = QPushButton("Refresh")
        self.copy_button = QPushButton("Copy Selected")

        layout.addWidget(self.list_widget)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.copy_button)
        self.setLayout(layout)

        self.refresh_button.clicked.connect(self.load_history)
        self.copy_button.clicked.connect(self.copy_selected)

        self.load_history()

    def load_history(self):
        self.list_widget.clear()
        entries = self.db.get_entries()
        for _id, content, ts in entries:
            self.list_widget.addItem(f"[{ts}] {content[:80]}")

    def copy_selected(self):
        item = self.list_widget.currentItem()
        if item:
            text = item.text().split("] ", 1)[-1]
            pyperclip.copy(text)

def run_ui():
    app = QApplication(sys.argv)
    window = ClipboardUI()
    window.show()
    sys.exit(app.exec_())
