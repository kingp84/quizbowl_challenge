# ui/components/tournament_progress.py

import streamlit as st

def render_tournament_progress(progress: dict | None):
    st.header("📈 Tournament Progress")

    if not progress:
        st.info("No tournament progress available yet.")
        return

    st.subheader("Rounds Completed")
    st.write(f"{progress.get('rounds_completed', 0)} / {progress.get('total_rounds', 0)}")

    st.subheader("Current Match")
    current = progress.get("current_match")
    if current:
        st.write(f"{current['team1']} vs {current['team2']} • Score: {current['score1']} - {current['score2']}")
    else:
        st.info("No active match right now.")