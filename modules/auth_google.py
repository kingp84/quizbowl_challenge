# modules/auth_google.py
import streamlit as st
from requests_oauthlib import OAuth2Session

# Load secure values from Streamlit secrets
GOOGLE_CLIENT_ID = st.secrets["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = st.secrets["GOOGLE_CLIENT_SECRET"]
REDIRECT_URI = st.secrets["REDIRECT_URI"]
REDIRECT_URI = "https://quizbowl-challenge.streamlit.app/"

AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
USERINFO_ENDPOINT = "https://openidconnect.googleapis.com/v1/userinfo"


def login_with_google():
    """
    Returns user_info dict on successful login, otherwise None.
    Designed to be called from app.py.
    """
    # ✅ Read query parameters at the very beginning
    params = st.query_params.to_dict()
    code_param = params.get("code")
    state_param = params.get("state")
    code = code_param[0] if isinstance(code_param, list) and code_param else None
    returned_state = state_param[0] if isinstance(state_param, list) and state_param else None

    if code:
        saved_state = st.session_state.get("oauth_state")
        if saved_state and returned_state and returned_state != saved_state:
            st.error("OAuth state mismatch. Try again.")
            return None

        oauth_client = OAuth2Session(GOOGLE_CLIENT_ID, redirect_uri=REDIRECT_URI)
        token = oauth_client.fetch_token(
            TOKEN_ENDPOINT,
            code=code,
            client_secret=GOOGLE_CLIENT_SECRET,
            include_client_id=True
        )

        resp = oauth_client.get(USERINFO_ENDPOINT, token=token)
        user_info = resp.json()
        st.session_state["user_info"] = user_info
        if "oauth_state" in st.session_state:
            del st.session_state["oauth_state"]
        return user_info

    # Not logged in: build the authorization URL safely using requests_oauthlib
    oauth = OAuth2Session(
        client_id=GOOGLE_CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=["openid", "email", "profile"]
    )

    auth_url, state = oauth.authorization_url(
        AUTHORIZATION_ENDPOINT,
        access_type="offline",
        prompt="consent"
    )

    # Persist state to validate callback later
    st.session_state["oauth_state"] = state

    # ✅ Only render the sign-in button (no debug text)
    st.markdown(f"""
        <a href="{auth_url}">
            <button style="font-size: 1.0rem; padding: 0.45rem 0.9rem; margin-top: 0.6rem;">
                Sign in with Google
            </button>
        </a>
    """, unsafe_allow_html=True)

    return None
