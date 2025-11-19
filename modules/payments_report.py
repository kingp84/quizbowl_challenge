# modules/payments_report.py

from modules.db import get_connection

def get_total_payments() -> float:
    with get_connection() as conn:
        row = conn.execute("SELECT SUM(amount) as total FROM payments").fetchone()
        return row["total"] if row else 0.0