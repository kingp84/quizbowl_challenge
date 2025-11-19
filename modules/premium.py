# modules/premium.py

from modules.db import get_connection

def is_premium(user_id: int) -> bool:
    with get_connection() as conn:
        row = conn.execute("SELECT premium FROM users WHERE id = ?", (user_id,)).fetchone()
        return bool(row["premium"]) if row else False