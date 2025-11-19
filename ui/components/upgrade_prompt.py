# ui/components/ungrade_prompt.py

import streamlit as st

def render_ungrade_prompt():
    st.header("📝 Ungraded Prompt")

    st.write("This section allows you to practice without grading. Type your response freely.")

    prompt = st.text_area("Your response", placeholder="Write your answer here...")
    if st.button("Submit"):
        st.info("Response recorded (not graded). Use this space for practice or brainstorming.")