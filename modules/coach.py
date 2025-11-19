# modules/coach.py

import sqlite3
from pathlib import Path

DB_PATH = Path("data/users.db")

def _conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = _conn()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT,
            premium BOOLEAN DEFAULT 0,
            school_name TEXT,
            city TEXT,
            state TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coach_email TEXT NOT NULL,
            team_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS promo_redemptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            code TEXT NOT NULL,
            redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def list_coach_teams(coach_email: str) -> list[dict]:
    with _conn() as conn:
        rows = conn.execute(
            "SELECT id, team_name FROM teams WHERE coach_email = ? ORDER BY created_at DESC",
            (coach_email,)
        ).fetchall()
        return [dict(row) for row in rows]

def get_or_create_team(coach_email: str, team_name: str) -> dict:
    with _conn() as conn:
        row = conn.execute(
            "SELECT id, team_name FROM teams WHERE coach_email = ? AND team_name = ?",
            (coach_email, team_name)
        ).fetchone()
        if row:
            return dict(row)
        conn.execute(
            "INSERT INTO teams (coach_email, team_name) VALUES (?, ?)",
            (coach_email, team_name)
        )
        conn.commit()
        new_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        return {"id": new_id, "team_name": team_name}

def update_school_info(user_id: int, school_name: str, city: str, state: str):
    conn = _conn()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users
        SET school_name = ?, city = ?, state = ?
        WHERE id = ?
    """, (school_name, city, state, user_id))
    conn.commit()
    conn.close()