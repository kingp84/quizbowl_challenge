# scripts/reset_promos.py
import sqlite3
from pathlib import Path

DB_PATH = Path("data/users.db")

def reset_promo_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop the old table if it exists
    cursor.execute("DROP TABLE IF EXISTS promo_codes")

    # Recreate with the correct schema
    cursor.execute("""
    CREATE TABLE promo_codes (
        code TEXT PRIMARY KEY,
        applies_to TEXT CHECK(applies_to IN ('individual','team')),
        max_uses INTEGER,
        uses INTEGER DEFAULT 0,
        expires_at TEXT
    )
    """)

    # Also ensure promo_redemptions exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS promo_redemptions (
        code TEXT,
        email TEXT,
        team_id INTEGER,
        redeemed_at TEXT
    )
    """)

    # Seed your first promo code
    cursor.execute("""
    INSERT INTO promo_codes (code, applies_to, max_uses, uses, expires_at)
    VALUES (?, ?, ?, ?, ?)
    """, ("OKLAHOMAQUIZBOWL", "team", 370, 0, "2025-12-31T23:59:59"))

    conn.commit()
    conn.close()
    print("Promo table reset and seed code added.")

if __name__ == "__main__":
    reset_promo_table()