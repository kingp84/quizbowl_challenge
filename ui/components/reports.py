# ui/components/reports.py

import streamlit as st
from modules.payments_report import get_total_payments
from modules.feedback import get_all_feedback

def render_reports(admin: bool):
    st.header("📊 Reports")

    if not admin:
        st.warning("You must be an admin to view reports.")
        return

    st.subheader("Payments Summary")
    total = get_total_payments()
    st.metric("Total Payments", f"${total:.2f}")

    st.subheader("Feedback Summary")
    feedback = get_all_feedback()
    st.write(f"Total feedback entries: {len(feedback)}")
    if feedback:
        st.write("Recent feedback:")
        for row in feedback[:5]:
            st.write(f"- {row['message']}")