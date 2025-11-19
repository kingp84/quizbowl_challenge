# modules/payments_split.py

from modules.db import get_connection

def split_payment(payer_id: int, recipients: list[int], total_amount: float):
    if not recipients:
        return

    share = round(total_amount / len(recipients), 2)

    with get_connection() as conn:
        for recipient_id in recipients:
            conn.execute("""
                INSERT INTO payment_splits (payer_id, recipient_id, amount)
                VALUES (?, ?, ?)
            """, (payer_id, recipient_id, share))
        conn.commit()

def get_splits_for_user(user_id: int) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT * FROM payment_splits
            WHERE payer_id = ? OR recipient_id = ?
            ORDER BY id DESC
        """, (user_id, user_id)).fetchall()
        return [dict(row) for row in rows]