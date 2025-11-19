# modules/stats.py

from modules.db import get_connection

def get_user_stats(user_id: int) -> dict:
    with get_connection() as conn:
        row = conn.execute("""
            SELECT COUNT(*) as games_played FROM hall_of_fame WHERE user_id = ?
        """, (user_id,)).fetchone()
        return {"games_played": row["games_played"] if row else 0}