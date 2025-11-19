# ui/components/promo_admin.py

import streamlit as st
from modules.promo import redeem_code
from modules.db import get_connection

def render_promo_admin(admin: bool):
    st.header("🎛️ Promo Code Admin")

    if not admin:
        st.warning("You must be an admin to view this page.")
        return

    st.subheader("Create Promo Code")
    code = st.text_input("Promo Code")
    if st.button("Add Promo Code"):
        if not code.strip():
            st.error("Please enter a code.")
        else:
            with get_connection() as conn:
                conn.execute("INSERT INTO promo_codes (code) VALUES (?)", (code.strip(),))
                conn.commit()
            st.success(f"Promo code '{code}' added.")

    st.subheader("Existing Promo Codes")
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM promo_codes ORDER BY id DESC").fetchall()
        for row in rows:
            st.write(f"- {row['code']}")