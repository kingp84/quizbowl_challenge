# ui/components/leaderboard_highlight.py

import streamlit as st
from modules.hall_of_fame import get_top_players

def render_leaderboard_highlight():
    st.header("📊 Leaderboard Highlights")

    top = get_top_players(limit=5)
    if not top:
        st.info("No leaderboard data yet.")
        return

    st.subheader("Top 5 Players")
    for i, row in enumerate(top, start=1):
        st.write(f"{i}. User {row['user_id']} • {row['wins']} wins ({row['format']})")