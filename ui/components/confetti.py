# ui/components/confetti.py

import streamlit as st

def render_confetti(trigger: bool = False):
    if trigger:
        st.balloons()
        st.success("🎉 Celebration triggered!")