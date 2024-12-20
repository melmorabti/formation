# Module: import_data.py
# Handles importing session data from an Excel file.

def import_sessions():
    st.title("Importer les sessions de formation")
    st.write("Chargez un fichier Excel contenant les sessions de formation extraites du SIRH.")

    uploaded_file = st.file_uploader("Choisir un fichier Excel", type=["xlsx"])

    if uploaded_file:
        try:
            # Load the Excel file into a Pandas DataFrame
            data = pd.read_excel(uploaded_file)
            st.success("Fichier importé avec succès !")
            st.dataframe(data.head())  # Display the first few rows for confirmation

            # Option to save the data for use in other pages
            if st.button("Enregistrer les données"):
                st.session_state["session_data"] = data
                st.success("Données enregistrées avec succès !")
        except Exception as e:
            st.error(f"Erreur lors de l'importation du fichier : {e}")