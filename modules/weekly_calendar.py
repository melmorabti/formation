from streamlit_calendar import calendar
import streamlit as st
import pandas as pd

def show_calendar():
    st.title("Planning hebdomadaire interactif")

    if "session_data" not in st.session_state:
        st.warning("Veuillez d'abord importer les données des sessions.")
        return

    data = st.session_state["session_data"]

    # Conversion des dates
    data["Début"] = pd.to_datetime(data["Début"], errors="coerce", format="%d/%m/%Y")
    data["Fin"] = pd.to_datetime(data["Fin"], errors="coerce", format="%d/%m/%Y")

    # Nettoyage des données essentielles
    cleaned = data.dropna(subset=["Nom de la formation", "Début", "Fin"]).copy()

    # Calcul de la durée en jours
    cleaned["Durée (jours)"] = (cleaned["Fin"] - cleaned["Début"]).dt.days

    # Séparer les courtes et longues sessions
    sessions_courtes = cleaned[cleaned["Durée (jours)"] <= 31]
    sessions_longues = cleaned[cleaned["Durée (jours)"] > 31]

    # Créer les événements pour le calendrier
    events = []
    for _, row in sessions_courtes.iterrows():
        try:
            organisme = row.get("Organisme de formation", "").strip()
            lieu = row.get("Lieu de formation", "").strip()
            
            event_title = f"{row['Nom de la formation']}"
            if organisme:
                event_title += f" - {organisme}"
            if lieu:
                event_title += f" @ {lieu}"
            
            events.append({
                "title": event_title,
                "start": row["Début"].strftime("%Y-%m-%dT%H:%M:%S"),
                "end": row["Fin"].strftime("%Y-%m-%dT%H:%M:%S")
            })
        except Exception as e:
            st.warning(f"Une session a été ignorée (problème de données) : {e}")

    # Options du calendrier
    options = {
        "locale": "fr",
        "firstDay": 1,
        "initialView": "timeGridWeek",
        "slotMinTime": "08:00:00",
        "slotMaxTime": "19:00:00",
        "hiddenDays": [0, 6],
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek"
        },
        "buttonText": {
            "today": "aujourd’hui",
            "month": "mois",
            "week": "semaine",
            "day": "jour",
            "list": "liste"
        }
    }

    # Affichage du calendrier
    if not events:
        st.info("Aucune session de moins d’un mois à afficher dans le calendrier.")
    else:
        calendar(events=events, options=options)

    # Affichage des sessions longues en bas
    if not sessions_longues.empty:
        st.subheader("📚 Formations longues (durée > 1 mois)")
        st.dataframe(
            sessions_longues[
                ["Nom de la formation", "Début", "Fin", "Durée (jours)", "Organisme de formation", "Lieu de formation"]
            ].sort_values(by="Début")
        )
