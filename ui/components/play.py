# ui/components/play.py

import streamlit as st
from ui.components.gameplay_loop import render_gameplay_loop
from ui.components.gameplay_ossaa import render_gameplay_ossaa
from ui.components.gameplay_froshmore import render_gameplay_froshmore

def render_play(user: dict | None):
    st.header("🎮 Play")

    mode = st.selectbox("Select Game Mode", ["Adaptive Loop", "OSSAA", "Froshmore"])

    if mode == "Adaptive Loop":
        render_gameplay_loop(user)
    elif mode == "OSSAA":
        render_gameplay_ossaa(user)
    elif mode == "Froshmore":
        render_gameplay_froshmore(user)