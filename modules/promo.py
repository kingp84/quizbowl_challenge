# modules/promo.py

from modules.db import get_connection

def redeem_code(user_id: int, code: str) -> bool:
    with get_connection() as conn:
        used = conn.execute(
            "SELECT * FROM promo_redemptions WHERE user_id = ? AND code = ?",
            (user_id, code)
        ).fetchone()
        if used:
            return False
        conn.execute(
            "INSERT INTO promo_redemptions (user_id, code) VALUES (?, ?)",
            (user_id, code)
        )
        conn.commit()
        return True