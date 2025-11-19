# modules/auth.py

import sqlite3
from pathlib import Path

DB_PATH = Path("data/users.db")

def _conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def authenticate(email: str, password: str) -> dict | None:
    with _conn() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?",
            (email, password)
        ).fetchone()
        return dict(row) if row else None