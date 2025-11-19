# ui/components/tournament_rewards.py

import streamlit as st
from modules.rewards import calculate_rewards

def render_tournament_rewards(user: dict | None, score: int = 0):
    st.header("🎖️ Tournament Rewards")

    if not user or "id" not in user:
        st.warning("You must be logged in to view rewards.")
        return

    rewards = calculate_rewards(score)
    st.success(f"User {user['id']} earned {rewards} reward points from this tournament!")