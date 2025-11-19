# modules/rooms.py

from modules.db import get_connection
import secrets

def create_room(user_id: int, format: str) -> str:
    code = secrets.token_hex(4)  # short unique code
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO rooms (code, format, created_by) VALUES (?, ?, ?)",
            (code, format, user_id)
        )
        conn.commit()
    return code

def join_room(code: str) -> dict | None:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM rooms WHERE code = ?", (code,)).fetchone()
        return dict(row) if row else None