import sqlite3
from datetime import datetime
from config import Config

DB_PATH = Config.DATABASE_PATH

def create_audit_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT,
                    action TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def log_action(user, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO audit_log (user, action, timestamp) VALUES (?, ?, ?)", (user, action, timestamp))
    conn.commit()
    conn.close()

