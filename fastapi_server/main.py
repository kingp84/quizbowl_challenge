# fastapi_server/main.py

import os
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from authlib.integrations.starlette_client import OAuth
from jose import jwt
from datetime import datetime, timedelta
from urllib.parse import urlencode
from fastapi import Header
from modules.square_flow import handle_square_webhook
from config.payment_settings import DONATION_ENDPOINT

@app.post("/webhooks/square")
async def square_webhook(request: Request, square_signature: str = Header(None)):
    payload = await request.body()
    result = handle_square_webhook(payload, square_signature, DONATION_ENDPOINT, PAYPAL_RECEIVE_EMAIL)
    return JSONResponse(result)

from config.settings import (
    GOOGLE_OAUTH_CLIENT_ID,
    GOOGLE_OAUTH_CLIENT_SECRET,
    OAUTH_REDIRECT_URI,
    ALLOWED_EMAIL_DOMAINS,
    SESSION_SECRET,
    SESSION_COOKIE_NAME,
    SESSION_COOKIE_SECURE,
    SESSION_COOKIE_SAMESITE,
    SESSION_COOKIE_MAX_AGE,
)

# Your Streamlit public URL (used to send the user back after sign-in)
STREAMLIT_APP_URL = "https://abcd1234.ngrok.io"

app = FastAPI()

# CORS (allow Streamlit app to call /session if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[STREAMLIT_APP_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth = OAuth()
oauth.register(
    name="google",
    client_id=GOOGLE_OAUTH_CLIENT_ID,
    client_secret=GOOGLE_OAUTH_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

def create_session_jwt(user):
    payload = {
        "sub": user["email"],
        "name": user["name"],
        "email": user["email"],
        "iat": int(datetime.utcnow().timestamp()),
        "exp": int((datetime.utcnow() + timedelta(days=7)).timestamp()),
    }
    return jwt.encode(payload, SESSION_SECRET, algorithm="HS256")

def parse_email_domain(email: str) -> str:
    return email.split("@")[-1].lower().strip()

@app.get("/login")
async def login(request: Request):
    # after login, send users back to Streamlit with a success flag
    next_url = STREAMLIT_APP_URL
    return await oauth.google.authorize_redirect(request, OAUTH_REDIRECT_URI + "?" + urlencode({"next": next_url}))

@app.get("/oauth/callback")
async def oauth_callback(request: Request):
    # Exchange the code for tokens and parse user info
    try:
        token = await oauth.google.authorize_access_token(request)
        userinfo = token.get("userinfo")
        if not userinfo:
            return JSONResponse({"error": "No userinfo"}, status_code=400)

        email = userinfo.get("email")
        name = userinfo.get("name") or email

        # Optional domain restriction
        if ALLOWED_EMAIL_DOMAINS:
            domain = parse_email_domain(email)
            if domain not in [d.lower() for d in ALLOWED_EMAIL_DOMAINS]:
                return JSONResponse({"error": "Domain not allowed"}, status_code=403)

        # Create session JWT and set cookie
        session_jwt = create_session_jwt({"email": email, "name": name})
        response = RedirectResponse(url=request.query_params.get("next") or STREAMLIT_APP_URL)
        response.set_cookie(
            key=SESSION_COOKIE_NAME,
            value=session_jwt,
            max_age=SESSION_COOKIE_MAX_AGE,
            secure=SESSION_COOKIE_SECURE,
            httponly=True,
            samesite=SESSION_COOKIE_SAMESITE,
        )
        return response

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

@app.get("/session")
def session(request: Request):
    # Returns current user from cookie
    cookie = request.cookies.get(SESSION_COOKIE_NAME)
    if not cookie:
        return JSONResponse({"authenticated": False})
    try:
        data = jwt.decode(cookie, SESSION_SECRET, algorithms=["HS256"])
        return JSONResponse({"authenticated": True, "email": data["email"], "name": data["name"]})
    except Exception:
        return JSONResponse({"authenticated": False})

@app.get("/logout")
def logout():
    # Clear session cookie and return to Streamlit
    response = RedirectResponse(url=STREAMLIT_APP_URL)
    response.delete_cookie(SESSION_COOKIE_NAME)
    return response

# Keep existing payment webhook routes here...