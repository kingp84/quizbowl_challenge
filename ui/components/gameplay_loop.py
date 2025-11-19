# ui/components/gameplay_loop.py

import streamlit as st
from modules.adaptive_engine import adjust_difficulty
from modules.packetloader import get_question

def render_gameplay_loop(user: dict | None):
    st.header("🎮 Gameplay Loop")

    if not user or "id" not in user:
        st.warning("You must be logged in to play.")
        return

    # Initialize session state
    if "difficulty" not in st.session_state:
        st.session_state.difficulty = "medium"
    if "current_question" not in st.session_state:
        st.session_state.current_question = None
    if "last_result" not in st.session_state:
        st.session_state.last_result = None

    # Get new question
    if st.button("Get Question"):
        q = get_question("NAQT", difficulty=st.session_state.difficulty)
        st.session_state.current_question = q
        st.session_state.last_result = None

    # Show question
    q = st.session_state.current_question
    if q:
        st.subheader("Question")
        st.write(q.get("text", "No text available."))

        user_answer = st.text_input("Your answer")
        if st.button("Check Answer"):
            correct = (user_answer or "").strip().lower() == (q.get("answer", "") or "").strip().lower()
            st.session_state.last_result = "correct" if correct else "incorrect"
            st.session_state.difficulty = adjust_difficulty(st.session_state.difficulty, correct)

    # Show result
    if st.session_state.last_result == "correct":
        st.success("Correct! 🎉")
    elif st.session_state.last_result == "incorrect":
        st.error("Incorrect. Try again!")
        with st.expander("Reveal answer"):
            st.write(q.get("answer", "No answer provided."))