import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

DB_PATH = Config.DATABASE_PATH

def create_user_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT
                )''')
    conn.commit()
    conn.close()

def add_user(username, password):
    hashed = generate_password_hash(password)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row:
        return check_password_hash(row[0], password)
    return False

