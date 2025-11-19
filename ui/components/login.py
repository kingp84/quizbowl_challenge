# ui/components/login.py

import streamlit as st
from modules.auth import authenticate

def render_login():
    st.header("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = authenticate(email, password)
        if user:
            st.session_state["user"] = user
            st.success(f"Welcome back, {user['name']}!")
        else:
            st.error("Invalid email or password.")