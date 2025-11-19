# ui/components/promo_redeem.py

import streamlit as st
from modules.promo import redeem_code

def render_promo_redeem(user: dict | None):
    st.header("🎟️ Redeem Promo Code")

    if not user or "id" not in user:
        st.warning("You must be logged in to redeem a promo code.")
        return

    code = st.text_input("Enter promo code")
    if st.button("Redeem"):
        if not code.strip():
            st.error("Please enter a code.")
        else:
            success = redeem_code(user["id"], code.strip())
            if success:
                st.success("Promo code redeemed successfully!")
            else:
                st.error("This code has already been used or is invalid.")