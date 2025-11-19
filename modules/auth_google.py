import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import os
import urllib.parse

# Load from Streamlit secrets or environment variables
GOOGLE_CLIENT_ID = st.secrets.get("GOOGLE_CLIENT_ID") or os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = st.secrets.get("GOOGLE_CLIENT_SECRET") or os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "https://quizbowl-challenge.streamlit.app"  # Replace with your actual Streamlit app URL

AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
USERINFO_ENDPOINT = "https://www.googleapis.com/oauth2/v3/userinfo"

def login_with_google():
    if "user_info" in st.session_state:
        return st.session_state["user_info"]

    query_params = st.query_params.to_dict()
    code = query_params.get("code")

    if code:
        # Exchange code for token
        client = OAuth2Session(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, redirect_uri=REDIRECT_URI)
        token = client.fetch_token(
            TOKEN_ENDPOINT,
            code=code,
            grant_type="authorization_code"
        )

        # Get user info
        resp = client.get(USERINFO_ENDPOINT, token=token)
        user_info = resp.json()
        st.session_state["user_info"] = user_info
        return user_info

    # Not logged in yet
    auth_url = (
        f"{AUTHORIZATION_ENDPOINT}?"
        f"response_type=code&"
        f"client_id={GOOGLE_CLIENT_ID}&"
        f"redirect_uri={urllib.parse.quote(REDIRECT_URI)}&"
        f"scope=openid%20email%20profile&"
        f"access_type=offline&"
        f"prompt=consent"
    )

    st.markdown(f"""
        <a href="{auth_url}">
            <button style="font-size: 1.2rem; padding: 0.5rem 1rem; margin-top: 1rem;">
                Sign in with Google
            </button>
        </a>
    """, unsafe_allow_html=True)

    return None