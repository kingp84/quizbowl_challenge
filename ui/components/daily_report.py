# ui/components/daily_report.py

import datetime
import streamlit as st
from modules.payments_report import get_total_payments
from modules.hall_of_fame import get_top_players

def render_daily_report(admin: bool):
    st.header("📅 Daily Report")

    if not admin:
        st.warning("You must be an admin to view the daily report.")
        return

    # Header summary
    today = datetime.date.today().strftime("%B %d, %Y")
    st.subheader(f"Summary for {today}")

    col1, col2 = st.columns(2)
    with col1:
        total = get_total_payments()
        st.metric(label="Total Payments Recorded", value=f"${total:.2f}")
    with col2:
        top = get_top_players(limit=5)
        st.write("Top Players (by wins):")
        if top:
            for row in top:
                st.write(f"- User {row['user_id']} • {row['format']} • {row['wins']} wins")
        else:
            st.info("No wins recorded yet.")

    st.divider()
    st.caption("This is a lightweight daily snapshot. Extend with traffic, sessions, and engagement metrics as needed.")