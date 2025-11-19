# modules/feature_requests.py

from modules.db import get_connection

def submit_feature_request(user_id: int, message: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO feature_requests (user_id, message) VALUES (?, ?)",
            (user_id, message)
        )
        conn.commit()