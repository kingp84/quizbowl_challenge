import streamlit as st
from ui.components import coach_dashboard, login, play, promo_redeem
from ui.components import feedback_section, feedback_dashboard, reports, promo_admin

# Utility function
def is_admin(email: str) -> bool:
    if not email:
        return False
    admins = ["patrick.e.king1958@gmail.com"]
    return email in admins

def main():
    st.set_page_config(page_title="Quizbowl Challenge", layout="wide")
    st.title("Quizbowl Challenge")

    # Use this for testing without login
    # user = {
    #     "id": 123,
    #     "name": "Patrick",
    #     "email": "patrick@example.com",
    #     "premium": True
    # }

    # Use this for production with login
    user = st.session_state.get("user")
    email = user["email"] if user else None
    admin = is_admin(email)

    st.sidebar.title("Quizbowl Challenge")
    page = st.sidebar.radio("Navigate", [
        "Login", "Play", "Coach Dashboard", "Promo Redeem", "Feedback", "Reports", "Admin"
    ])

    if page == "Login":
        login.render_login()
    elif page == "Play":
        play.render_play(user)
    elif page == "Coach Dashboard":
        coach_dashboard.render_coach_dashboard(user)
    elif page == "Promo Redeem":
        promo_redeem.render_promo_redeem(user)
    elif page == "Feedback":
        feedback_section.render_feedback_section(user)
        if admin:
            feedback_dashboard.render_feedback_dashboard()
    elif page == "Reports":
        reports.render_reports(admin)
    elif page == "Admin":
        promo_admin.render_promo_admin(admin)

if __name__ == "__main__":
    main()