# ui/components/champion_announcement.py

import streamlit as st

def render_champion_announcement(champion_team: str | None):
    st.header("🥇 Champion Announcement")

    if not champion_team:
        st.info("No champion has been declared yet.")
        return

    st.success(f"Congratulations to **{champion_team}** for winning the tournament!")