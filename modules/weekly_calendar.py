# Module: weekly_calendar.py
# Displays a weekly calendar of training sessions with an interactive calendar.

from streamlit_calendar import calendar
import streamlit as st
import pandas as pd

def show_calendar():
    st.title("Planning hebdomadaire interactif")

    if "session_data" not in st.session_state:
        st.warning("Veuillez d'abord importer les données des sessions.")
        return

    data = st.session_state["session_data"]

    data["Début"] = pd.to_datetime(data["Début"], errors="coerce", format="%d/%m/%Y")
    data["Fin"] = pd.to_datetime(data["Fin"], errors="coerce", format="%d/%m/%Y")

    cleaned = data.dropna(subset=["Nom de la formation", "Début", "Fin"])

    events = []
    for _, row in cleaned.iterrows():
        try:
            events.append({
                "title": str(row["Nom de la formation"]),
                "start": row["Début"].strftime("%Y-%m-%dT%H:%M:%S"),
                "end": row["Fin"].strftime("%Y-%m-%dT%H:%M:%S")
            })
        except Exception as e:
            st.warning(f"Une session a été ignorée (problème de données) : {e}")

    # Configuration du calendrier en français et commençant le lundi
options = {
    "locale": "fr",
    "firstDay": 1,
    "initialView": "timeGridWeek",
    "slotMinTime": "08:00:00",     # Heure de début d'affichage
    "slotMaxTime": "19:00:00",     # Heure de fin d'affichage
    "hiddenDays": [0, 6],          # Cache le dimanche (0) et le samedi (6)
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek"
    }
}


    if not events:
        st.info("Aucune session valide à afficher dans le calendrier.")
    else:
        calendar(events=events, options=options)
