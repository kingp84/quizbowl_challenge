# ui/components/hall_of_fame.py

import streamlit as st
from modules.hall_of_fame import get_top_players

def render_hall_of_fame():
    st.header("🏆 Hall of Fame")

    top = get_top_players(limit=10)
    if not top:
        st.info("No players recorded yet.")
        return

    for row in top:
        st.write(f"User {row['user_id']} • Format: {row['format']} • Wins: {row['wins']}")