import streamlit as st
from modules.auth_google import login_with_google
from modules.ui_utils import set_background
from modules.game_ui import game_ui

# --- Background selector ---
bg_choice = st.selectbox("Choose a background theme", ["Default", "Tournament", "Trivia"])
bg_map = {
    "Default": "assets/default_bg.png",
    "Tournament": "assets/tournament_bg.png",
    "Trivia": "assets/trivia_bg.png"
}
set_background(bg_map[bg_choice])

# --- Google OAuth login ---
user = login_with_google()

# --- Sidebar logout ---
if "user_info" in st.session_state:
    if st.sidebar.button("Logout"):
        del st.session_state["user_info"]
        st.experimental_rerun()

# --- Game UI if logged in ---
if user:
    st.success(f"Welcome, {user['name']} ({user['email']})")
    game_ui(user)
else:
    st.info("Please sign in with Google to begin.")

