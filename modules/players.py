# modules/players.py

from modules.db import get_connection

def get_player(user_id: int) -> dict:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return dict(row) if row else {}