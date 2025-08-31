import os
import sqlite3


DB_FOLDER = os.path.join(os.path.dirname(__file__), "../files")
os.makedirs(DB_FOLDER, exist_ok=True)
DB_PATH = os.path.join(DB_FOLDER, "scam_db.db")

def init_db():
    """Create the database and tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reported_scams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text_content TEXT,
        ocr_text TEXT,
        factors TEXT,
        scammer_email TEXT,
        scammer_company TEXT,
        scammer_phone TEXT,
        raw_output TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
