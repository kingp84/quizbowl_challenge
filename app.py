import streamlit as st
import time
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
if "user_info" not in st.session_state:
    user = login_with_google()
else:
    user = st.session_state["user_info"]

# --- Custom laurel wreath spinner HTML ---
spinner_html = """
<div class="laurel-spinner">
  <img src="assets/laurel_wreath.svg" alt="Laurel Wreath" />
</div>
<style>
.laurel-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 150px;
  margin-top: 2rem;
}
.laurel-spinner img {
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
</style>
"""

# --- Main app flow ---
if "user_info" in st.session_state:
    st.success(f"Welcome {st.session_state['user_info']['email']}")

    # --- Game setup menu ---
    st.header("Choose Your Game Mode")

    mode = st.radio("Select mode:", ["Single Player", "Multiplayer", "Tournament"])
    format = st.selectbox("Competition Format:", ["Trivia", "NAQT", "OSSAA", "Froshmore"])
    difficulty = st.slider("Difficulty Level", 1, 10, 5)

    # Premium lock example
    premium_mode = st.checkbox("Team Mode 🔒")
    if premium_mode:
        st.warning("This feature requires Premium. Please upgrade to unlock.")

    # Continue button
    if st.button("Start Game"):
        # Show spinner while preparing
        spinner_placeholder = st.empty()
        spinner_placeholder.markdown(spinner_html, unsafe_allow_html=True)
        time.sleep(3)
        spinner_placeholder.empty()

        # Launch game UI with chosen settings
        game_ui(mode=mode, format=format, difficulty=difficulty)
else:
    st.info("Please log in to continue.")



