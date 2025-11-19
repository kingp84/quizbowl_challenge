# ui/components/feedback_dashboard.py

import streamlit as st
from modules.feedback import get_all_feedback

def render_feedback_dashboard(admin: bool):
    st.header("🗂️ Feedback Dashboard")

    if not admin:
        st.warning("You must be an admin to view the feedback dashboard.")
        return

    rows = get_all_feedback()
    if not rows:
        st.info("No feedback has been submitted yet.")
        return

    st.subheader("All Feedback")
    for row in rows:
        st.markdown(f"**User ID:** {row.get('user_id', '—')}  •  **ID:** {row.get('id', '—')}")
        st.write(row.get("message", ""))
        st.divider()