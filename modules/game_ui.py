import streamlit as st

def game_ui(user):
    st.title("🏆 Quizbowl Challenge")
    st.write(f"Welcome, {user['name']}! Let's set up your game.")

    # Tournament setup
    tournament_name = st.text_input("Tournament name", "Froshmore Invitational")
    round_number = st.selectbox("Round number", list(range(1, 11)))

    # Team setup
    col1, col2 = st.columns(2)
    with col1:
        team_a = st.text_input("Team A name", "North HS")
    with col2:
        team_b = st.text_input("Team B name", "South HS")

    # Background theme
    bg_choice = st.radio("Choose a background theme", ["Default", "Tournament", "Trivia"])
    bg_map = {
        "Default": "assets/default_bg.png",
        "Tournament": "assets/tournament_bg.png",
        "Trivia": "assets/trivia_bg.png"
    }
    from modules.ui_utils import set_background
    set_background(bg_map[bg_choice])

    # Confirm setup
    if st.button("Start Round"):
        st.success(f"🎉 Round {round_number} of {tournament_name} is ready!")
        st.write(f"Matchup: **{team_a}** vs **{team_b}**")
        # TODO: Load questions, scoring, and gameplay modules here
