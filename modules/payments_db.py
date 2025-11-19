# modules/payments_db.py

from modules.db import get_connection

def record_payment(user_id: int, amount: float):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO payments (user_id, amount) VALUES (?, ?)",
            (user_id, amount)
        )
        conn.commit()