# ui/components/tournament_leaderboard.py

import streamlit as st
from modules.hall_of_fame import get_top_players

def render_tournament_leaderboard():
    st.header("🏆 Tournament Leaderboard")

    top = get_top_players(limit=10)
    if not top:
        st.info("No tournament results yet.")
        return

    st.subheader("Top Players")
    for i, row in enumerate(top, start=1):
        st.write(f"{i}. User {row['user_id']} • {row['wins']} wins ({row['format']})")