# modules/stats_update.py

from modules.db import get_connection

def increment_stat(user_id: int, stat: str):
    with get_connection() as conn:
        conn.execute(f"""
            UPDATE users SET {stat} = {stat} + 1 WHERE id = ?
        """, (user_id,))
        conn.commit()