# ui/main.py
import streamlit as st
from modules.db import is_premium_account
# ui/main.py (snippet)
from ui.components.upgrade_prompt import render_upgrade_prompt
from modules.db import is_premium_account
# ui/main.py (snippets showing integration)
import streamlit as st
from modules.db import is_premium_account, is_admin
from ui.components.coach_dashboard import render_coach_dashboard
from ui.components.feedback_section import render_feedback_section
from ui.components.feedback_dashboard import render_feedback_dashboard
from ui.components.promo_redeem import render_promo_redeem
from ui.components.daily_report import render_daily_report
from ui.components.admin_reconcile import render_admin_reconcile
from ui.components.promo_admin import render_promo_admin

def render_main():
    user = st.session_state.get("user")
    email = user["email"] if user else None
    admin = is_admin(email) if email else False

    # ... existing sections ...

    st.divider()
    render_promo_admin(admin)

def render_main():
    user = st.session_state.get("user")
    email = user["email"] if user else None
    admin = is_admin(email) if email else False
    premium = is_premium_account(email) if email else False

    st.header("Quizbowl Challenge")

    # Coach dashboard (Premium)
    if email and premium:
        render_coach_dashboard(email)
    else:
        st.info("Sign in and upgrade to access coach tools.")

    st.divider()
    render_feedback_section(email if email else None)

    st.divider()
    st.subheader("Promos")
    team_id_for_promo = None
    render_promo_redeem(email if email else "", team_id=team_id_for_promo)

    st.divider()
    render_feedback_dashboard(admin)

    st.divider()
    render_daily_report(admin)

    st.divider()
    render_admin_reconcile(admin)

def render_main():
    user = st.session_state.get("user")
    email = user["email"] if user else None

    st.header("Quizbowl Challenge")

    if email and is_premium_account(email):
        st.success("Premium active—coach tools unlocked.")
        # show dashboards...
    else:
        st.info("Free mode active. Upgrade to unlock tournaments, coach dashboards, invoices, and avatars.")
        render_upgrade_prompt(email)

def render_main():
    user = st.session_state.get("user")
    email = user["email"] if user else None

    st.header("Welcome to Quizbowl Challenge")

    if email and is_premium_account(email):
        st.subheader("Coach Dashboard")
        st.write("Premium-only features go here.")
    else:
        st.info("Upgrade to Premium to unlock coach dashboards, tournaments, and invoices.")

# ui/main.py (snippet)
from ui.components.invoice_download import render_invoice_tools

def render_main():
    user = st.session_state.get("user")
    email = user["email"] if user else None

    # ... your premium gating
    # if premium:
    render_invoice_tools()