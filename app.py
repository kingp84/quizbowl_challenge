import streamlit as st
from modules.auth import init_user_db, register_user, login_user
from modules.ui_utils import set_background

# Background selector
bg_choice = st.selectbox("Choose a background theme", ["Default", "Tournament", "Trivia"])

# Map choice to image path
bg_map = {
    "Default": "assets/default_bg.png",
    "Tournament": "assets/tournament_bg.png",
    "Trivia": "assets/trivia_bg.png"
}

# Set background based on selection
set_background(bg_map[bg_choice])

# Initialize user database
init_user_db()

# App title
st.title("🎯 Quizbowl Challenge")

# Choose between login and registration
mode = st.radio("Choose mode", ["Login", "Register"], horizontal=True)

# User input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Session state to track login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# Registration flow
if mode == "Register":
    if st.button("Register"):
        if username and password:
            success, message = register_user(username, password)
            st.success(message) if success else st.error(message)
        else:
            st.warning("Please enter both username and password.")

# Login flow
elif mode == "Login":
    if st.button("Login"):
        if username and password:
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success(f"Welcome, {username}!")
            else:
                st.error("Invalid credentials.")
        else:
            st.warning("Please enter both username and password.")

# Post-login content
if st.session_state.logged_in:
    st.subheader("🏆 Dashboard")
    st.write(f"You're logged in as **{st.session_state.user}**.")
    # Placeholder for gameplay or dashboard modules
    st.info("Game modules coming soon!")
