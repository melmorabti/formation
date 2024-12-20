# Module: session_list.py
# Displays a list of all training sessions with filtering options.

def show_session_list():
    import pandas as pd
    import streamlit as st

    st.title("Liste des sessions de formation")

    # Check if session data exists
    if "session_data" not in st.session_state:
        st.warning("Veuillez d'abord importer les données des sessions.")
        return

    data = st.session_state["session_data"]

    # Filters
    st.sidebar.header("Filtres")
    organisme = st.sidebar.text_input("Organisme de formation")
    mode = st.sidebar.selectbox("Mode de formation", ["", "Présentiel", "E-learning"])

    # Apply filters
    filtered_data = data.copy()
    if organisme:
        filtered_data = filtered_data[filtered_data["Organisme de formation"].str.contains(organisme, na=False)]
    if mode:
        filtered_data = filtered_data[filtered_data["Mode formation"] == mode]

    # Display data
    if filtered_data.empty:
        st.info("Aucune session ne correspond aux filtres sélectionnés.")
    else:
        st.dataframe(filtered_data)
