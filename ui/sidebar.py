# ui/sidebar.py

import streamlit as st
from modules.auth import handle_oauth_callback, login_button, logout_button
from modules.db import is_premium_account, is_admin

def render_sidebar():
    st.sidebar.title("Quizbowl Challenge")

    # Always check session at load
    handle_oauth_callback()

    user = st.session_state.get("user")

    if user:
        st.sidebar.success(f"Signed in as {user['name']} ({user['email']})")
        logout_button()
    else:
        st.sidebar.info("You're not signed in.")
        login_button()

    # Show status badges
    email = user["email"] if user else None
    if email:
        premium = is_premium_account(email)
        admin = is_admin(email)

        if premium:
            st.sidebar.markdown("✅ **Premium Active**")
        else:
            st.sidebar.markdown("🔒 **Free Mode** — upgrade to unlock coach tools, tournaments, and invoices.")

        if admin:
            st.sidebar.markdown("🛠️ **Admin Tools Enabled**")

    # Mode selector (Phase 5 will use this)
    st.sidebar.header("Modes")
    st.session_state["mode"] = st.sidebar.selectbox(
        "Choose a mode",
        ["NAQT", "OSSAA", "Froshmore", "Trivia", "Tournament"],
        index=0,
    )