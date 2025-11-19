# modules/feedback.py

from modules.db import get_connection

def submit_feedback(user_id: int, message: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO feedback (user_id, message) VALUES (?, ?)",
            (user_id, message)
        )
        conn.commit()

def get_all_feedback() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM feedback ORDER BY id DESC").fetchall()
        return [dict(row) for row in rows]