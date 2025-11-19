# modules/matchmaking.py

from modules.db import get_connection

def queue_player(user_id: int, format: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO matchmaking_queue (user_id, format) VALUES (?, ?)",
            (user_id, format)
        )
        conn.commit()

def get_next_match(format: str) -> list[int]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT user_id FROM matchmaking_queue WHERE format = ? LIMIT 2",
            (format,)
        ).fetchall()
        return [row["user_id"] for row in rows]