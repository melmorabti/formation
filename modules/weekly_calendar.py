# Module: weekly_calendar.py
# Displays a weekly calendar of training sessions with an interactive calendar.

from streamlit_calendar import calendar
import streamlit as st
import pandas as pd

def show_calendar():
    st.title("Planning hebdomadaire interactif")

    # Vérifie si les données des sessions existent
    if "session_data" not in st.session_state:
        st.warning("Veuillez d'abord importer les données des sessions.")
        return

    # Charger les données des sessions
    data = st.session_state["session_data"]

    # Convertir les colonnes de dates en datetime
    data["Début"] = pd.to_datetime(data["Début"], errors="coerce", format="%d/%m/%Y")
    data["Fin"] = pd.to_datetime(data["Fin"], errors="coerce", format="%d/%m/%Y")

    # Créer des événements pour le calendrier
    events = []
    for _, session in data.iterrows():
        events.append({
            "title": session["Nom de la formation"],
            "start": session["Début"].strftime("%Y-%m-%dT%H:%M:%S"),
            "end": session["Fin"].strftime("%Y-%m-%dT%H:%M:%S"),
        })

    # Afficher le calendrier avec les événements
    calendar(events)

