# Module: import_data.py
# Handles importing session data from an Excel file.

import streamlit as st
import pandas as pd
import warnings

# Ignorer les avertissements liés à openpyxl
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

def import_sessions():
    st.title("Importer les sessions de formation")
    uploaded_file = st.file_uploader("Choisir un fichier Excel", type=["xlsx"])

    if uploaded_file:
        try:
            # Charger le fichier Excel
            data = pd.read_excel(uploaded_file, engine="openpyxl")
            st.success("Fichier importé avec succès !")
            st.dataframe(data.head())  # Affiche un aperçu des données
            st.session_state["session_data"] = data
        except Exception as e:
            st.error(f"Erreur lors de l'importation du fichier : {e}")
