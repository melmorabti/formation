# Module: weekly_calendar.py
# Displays a weekly calendar of training sessions.

def show_calendar():
    import pandas as pd
    from datetime import datetime, timedelta
    import streamlit as st

    st.title("Planning hebdomadaire")

    # Check if session data exists
    if "session_data" not in st.session_state:
        st.warning("Veuillez d'abord importer les données des sessions.")
        return

    data = st.session_state["session_data"]

    # Convert date columns to datetime
    data["Début"] = pd.to_datetime(data["Début"], errors="coerce", format="%d/%m/%Y")
    data["Fin"] = pd.to_datetime(data["Fin"], errors="coerce", format="%d/%m/%Y")

    # Get current week range
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=4)

    st.write(f"Semaine du {start_of_week.strftime('%d/%m/%Y')} au {end_of_week.strftime('%d/%m/%Y')}")

    # Filter sessions for the current week
    weekly_sessions = data[(data["Début"] >= start_of_week) & (data["Début"] <= end_of_week)]

    if weekly_sessions.empty:
        st.info("Aucune session prévue cette semaine.")
    else:
        for _, session in weekly_sessions.iterrows():
            st.write(f"**{session['Nom de la formation']}**")
            st.write(f"Dates : {session['Début'].strftime('%d/%m/%Y')} au {session['Fin'].strftime('%d/%m/%Y')}")
            st.write(f"Organisme : {session['Organisme de formation']}")
            st.write(f"Lieu : {session['Lieu de formation']}\n")

    # Navigation buttons for previous and next weeks
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Semaine précédente"):
            st.session_state["current_week"] = start_of_week - timedelta(days=7)
    with col2:
        if st.button("Semaine suivante"):
            st.session_state["current_week"] = start_of_week + timedelta(days=7)
