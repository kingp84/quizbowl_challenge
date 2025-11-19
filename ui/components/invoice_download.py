# ui/components/invoice_download.py

import streamlit as st
from modules.invoices import get_user_invoices

def render_invoice_download(user: dict | None):
    st.header("🧾 Invoice Download")

    if not user or "id" not in user:
        st.warning("You must be logged in to view invoices.")
        return

    invoices = get_user_invoices(user["id"])
    if not invoices:
        st.info("No invoices found.")
        return

    for inv in invoices:
        st.write(f"Invoice #{inv['id']} • ${inv['amount']:.2f} • {inv['description']}")
        st.download_button(
            label="Download Invoice",
            data=f"Invoice #{inv['id']}\nAmount: ${inv['amount']:.2f}\nDescription: {inv['description']}",
            file_name=f"invoice_{inv['id']}.txt"
        )