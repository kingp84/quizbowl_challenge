# ui/components/feature_requests_tab.py

import streamlit as st
from modules.feature_requests import submit_feature_request

def render_feature_requests_tab(user: dict | None):
    st.header("💡 Feature Requests")

    if not user or "id" not in user:
        st.warning("You must be logged in to submit feature requests.")
        return

    st.write("Tell us what would make Quizbowl Challenge better for you and your team.")

    message = st.text_area("Your request", placeholder="Describe the feature, why it matters, and any examples.")
    if st.button("Submit request"):
        if not message.strip():
            st.error("Please enter a feature request before submitting.")
        else:
            submit_feature_request(user["id"], message.strip())
            st.success("Thanks! Your feature request has been submitted.")