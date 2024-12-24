# Main file: main.py
# This file will orchestrate the Streamlit application.

import streamlit as st
from modules.import_data import import_sessions
from modules.weekly_calendar import show_calendar
from modules.session_list import show_session_list

# Set up Streamlit page config
st.set_page_config(
    page_title="Planning des Formations",
    layout="wide"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Importer les sessions", "Planning hebdomadaire", "Liste des sessions"])

# Navigation logic
if page == "Importer les sessions":
    import_sessions()
elif page == "Planning hebdomadaire":
    show_calendar()
elif page == "Liste des sessions":
    show_session_list()
