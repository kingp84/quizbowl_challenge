# ui/components/gameplay_naqt.py

import streamlit as st
from modules.gameplay_naqt import get_naqt_question

def render_gameplay_naqt(user: dict | None):
    st.header("🧠 NAQT Gameplay")

    difficulty = st.selectbox("Select difficulty", ["easy", "medium", "hard"], index=1)

    if st.button("Get Question"):
        q = get_naqt_question(difficulty)
        st.session_state.naqt_q = q

    q = st.session_state.get("naqt_q")
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