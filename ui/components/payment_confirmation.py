# ui/components/payment_confirmation.py

import streamlit as st
from modules.payments_controller import process_payment

def render_payment_confirmation(user: dict | None, cart: list[dict]):
    st.header("💳 Payment Confirmation")

    if not user or "id" not in user:
        st.warning("You must be logged in to confirm payment.")
        return

    if not cart:
        st.info("Your cart is empty.")
        return

    total = process_payment(user["id"], cart)
    st.success(f"Payment of ${total:.2f} confirmed for user {user['id']}.")