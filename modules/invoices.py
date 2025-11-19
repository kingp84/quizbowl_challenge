# modules/invoices.py

from modules.db import get_connection

def create_invoice(user_id: int, amount: float, description: str):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO invoices (user_id, amount, description)
            VALUES (?, ?, ?)
        """, (user_id, amount, description))
        conn.commit()

def get_user_invoices(user_id: int) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM invoices WHERE user_id = ? ORDER BY id DESC",
            (user_id,)
        ).fetchall()
        return [dict(row) for row in rows]