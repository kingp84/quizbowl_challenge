# ui/components/school_info_form.py

import streamlit as st
from modules.coach import update_school_info

def render_school_info_form(user: dict | None):
    st.subheader("🏫 School Information")

    if not user or "id" not in user:
        st.warning("You must be logged in to update school info.")
        return

    school_name = st.text_input("School Name", value=user.get("school_name", ""))
    city = st.text_input("City", value=user.get("city", ""))
    state = st.text_input("State", value=user.get("state", ""))

    if st.button("Update School Info"):
        if not school_name or not city or not state:
            st.error("Please fill in all fields.")
        else:
            update_school_info(user["id"], school_name, city, state)
            st.success("School information updated successfully!")