# ui/components/admin_reconcile.py

import streamlit as st
from modules.payments_report import get_total_payments
from modules.payments_db import record_payment

def render_admin_reconcile(admin: bool):
    st.header("💼 Admin Reconciliation")

    if not admin:
        st.warning("You must be an admin to view this page.")
        return

    st.subheader("Total Payments")
    total = get_total_payments()
    st.info(f"Total payments recorded: ${total:.2f}")

    st.subheader("Manual Adjustment")
    user_id = st.number_input("User ID", min_value=1, step=1)
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    if st.button("Record Adjustment"):
        record_payment(user_id, amount)
        st.success(f"Recorded adjustment of ${amount:.2f} for user {user_id}.")