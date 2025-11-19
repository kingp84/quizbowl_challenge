# ui/components/brackets_ui.py

import streamlit as st

def render_brackets_ui(teams: list[str]):
    st.header("🏆 Tournament Brackets")

    if not teams:
        st.warning("No teams registered yet.")
        return

    st.subheader("Registered Teams")
    for team in teams:
        st.write(f"- {team}")

    st.subheader("Bracket Simulation")
    if st.button("Generate Bracket"):
        st.success("Bracket generated! (stub logic)")
        # TODO: implement actual bracket generation