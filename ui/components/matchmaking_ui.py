# ui/components/matchmaking_ui.py

import streamlit as st
from modules.matchmaking import queue_player, get_next_match

def render_matchmaking_ui(user: dict | None):
    st.header("🤝 Matchmaking")

    if not user or "id" not in user:
        st.warning("You must be logged in to join matchmaking.")
        return

    format = st.selectbox("Select format", ["NAQT", "OSSAA", "Froshmore"])

    if st.button("Join Queue"):
        queue_player(user["id"], format)
        st.success(f"You have joined the {format} queue.")

    if st.button("Find Match"):
        players = get_next_match(format)
        if len(players) == 2:
            st.success(f"Match found: User {players[0]} vs User {players[1]}")
        else:
            st.info("Not enough players in the queue yet.")