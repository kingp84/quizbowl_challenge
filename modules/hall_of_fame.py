# modules/hall_of_fame.py

from modules.db import get_connection

def record_win(user_id: int, format: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO hall_of_fame (user_id, format) VALUES (?, ?)",
            (user_id, format)
        )
        conn.commit()

def get_top_players(limit: int = 10) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT user_id, format, COUNT(*) as wins
            FROM hall_of_fame
            GROUP BY user_id, format
            ORDER BY wins DESC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(row) for row in rows]