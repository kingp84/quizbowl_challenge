# ui/components/feedback_section.py

import streamlit as st
from modules.feedback import submit_feedback

def render_feedback_section(user: dict | None):
    st.header("🗣️ Share Feedback")

    if not user or "id" not in user:
        st.warning("You must be logged in to submit feedback.")
        return

    st.write("Help us improve. What’s working? What’s confusing? What would you change?")

    category = st.selectbox(
        "Category",
        ["General", "UI/UX", "Gameplay", "Packets", "Payments", "Coach Tools", "Other"]
    )
    message = st.text_area("Your feedback", placeholder="Be specific. Examples help us act quickly.")

    if st.button("Submit feedback"):
        text = f"[{category}] {message}".strip()
        if not message.strip():
            st.error("Please enter feedback before submitting.")
        else:
            submit_feedback(user["id"], text)
            st.success("Thanks! Your feedback has been submitted.")