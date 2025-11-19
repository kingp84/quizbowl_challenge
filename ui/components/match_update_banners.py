# ui/components/match_update_banners.py

import streamlit as st

def render_match_update_banners(match_info: dict | None):
    st.header("📢 Match Updates")

    if not match_info:
        st.info("No match updates available.")
        return

    st.success(f"Match between {match_info['team1']} and {match_info['team2']} is underway!")
    st.write(f"Current score: {match_info['score1']} - {match_info['score2']}")