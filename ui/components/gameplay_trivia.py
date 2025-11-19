# ui/components/gameplay_trivia.py

import streamlit as st
from modules.trivia_loader import get_question

def render_gameplay_trivia(user: dict | None):
    st.header("🎲 Trivia Gameplay")

    difficulty = st.selectbox("Select difficulty", ["easy", "medium", "hard"], index=1)

    if st.button("Get Question"):
        q = get_question(difficulty)
        st.session_state.trivia_q = q

    q = st.session_state.get("trivia_q")
    if q:
        st.subheader("Question")
        st.write(q.get("text", "No text available."))

        user_answer = st.text_input("Your answer")
        if st.button("Check Answer"):
            correct = (user_answer or "").strip().lower() == (q.get("answer", "") or "").strip().lower()
            if correct:
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect.")
                with st.expander("Reveal answer"):
                    st.write(q.get("answer", "No answer provided."))