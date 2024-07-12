
import streamlit as st
import pandas as pd
import random

# Données d'exemple
data = {
    'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai'],
    'Ventes': [random.randint(100, 500) for _ in range(5)],
}
df = pd.DataFrame(data)

# Titre de l'application
st.title("Test d'embed Streamlit")

# Sélection du mois
mois_selectionne = st.selectbox('Sélectionnez un mois :', df['Mois'].unique())

# Filtrage des données en fonction du mois sélectionné
df_filtre = df[df['Mois'] == mois_selectionne]

# Affichage du graphique
st.bar_chart(df_filtre.set_index('Mois'))

