import streamlit as st

def game_ui(user):
    st.title("Welcome to Quizbowl Challenge!")
    st.write(f"Hello, {user['username']}! Ready to play?")
    # Add game mode selection, question loading, etc.