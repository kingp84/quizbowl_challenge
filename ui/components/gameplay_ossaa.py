# ui/components/gameplay_ossaa.py

import streamlit as st
from modules.gameplay_ossaa import get_ossaa_question

def render_gameplay_ossaa(user: dict | None):
    st.header("🏅 OSSAA Gameplay")

    difficulty = st.selectbox("Select difficulty", ["easy", "medium", "hard"], index=1)

    if st.button("Get Question"):
        q = get_ossaa_question(difficulty)
        st.session_state.ossaa_q = q

    q = st.session_state.get("ossaa_q")
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