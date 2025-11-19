# scripts/seed_promos.py
import sqlite3
from pathlib import Path

DB_PATH = Path("data/users.db")

def seed_promo():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    INSERT INTO promo_codes (code, applies_to, max_uses, uses, expires_at)
    VALUES (?, ?, ?, ?, ?)
    """, ("OKLAHOMAQUIZBOWL", "team", 370, 0, "2025-12-31T23:59:59"))
    conn.commit()
    conn.close()
    print("Promo code seeded successfully.")

if __name__ == "__main__":
    seed_promo()