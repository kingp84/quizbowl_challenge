# ui/components/gameplay_froshmore.py

import streamlit as st

# Handle prior module naming (frosmore vs froshmore)
try:
    from modules.gameplay_frosmore import get_question as get_froshmore_question
except ImportError:
    from modules.gameplay_frosmore import get_question as get_froshmore_question  # fallback to same name

def render_gameplay_froshmore(user: dict | None):
    st.header("🏁 Froshmore Gameplay")

    # Difficulty selection
    difficulty = st.selectbox("Select difficulty", ["easy", "medium", "hard"], index=1)

    # Ensure session state
    if "frosh_q" not in st.session_state:
        st.session_state.frosh_q = None
    if "frosh_result" not in st.session_state:
        st.session_state.frosh_result = None

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Get question"):
            q = get_froshmore_question(difficulty=difficulty)
            st.session_state.frosh_q = q
            st.session_state.frosh_result = None

    with col2:
        if st.button("Next"):
            q = get_froshmore_question(difficulty=difficulty)
            st.session_state.frosh_q = q
            st.session_state.frosh_result = None

    # Show question
    q = st.session_state.frosh_q
    if not q:
        st.info("Choose a difficulty and click Get question to begin.")
        return

    st.subheader("Question")
    st.write(q.get("text", "No question text."))

    # Answer input and check
    user_answer = st.text_input("Your answer")
    if st.button("Check answer"):
        correct = (user_answer or "").strip().lower() == (q.get("answer", "") or "").strip().lower()
        st.session_state.frosh_result = "correct" if correct else "incorrect"

    # Result and reveal
    result = st.session_state.frosh_result
    if result == "correct":
        st.success("Correct! 🎉")
    elif result == "incorrect":
        st.error("Not quite. Keep going!")
        with st.expander("Reveal answer"):
            st.write(q.get("answer", "No answer provided."))