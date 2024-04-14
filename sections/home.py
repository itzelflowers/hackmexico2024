import streamlit as st
from sections import maps

def app():
    st.title("Bienvenidos a Hidden Places")
    # Crear dos columnas para la descripción y el mapa
    col1, col2 = st.columns([2, 3])  # Proporción de columnas: 2 para descripción, 3 para el mapa

    with col1:
        st.subheader("Explora sin Límites 🌍")
        st.write("""
        **Hidden Places** es tu guía para un turismo accesible en la CDMX. ✨ Nos comprometemos a que personas con discapacidad motriz y adultos mayores disfruten de cada rincón con **total libertad**. 🚶‍♂️🚶‍♀️

        Accede a información de destinos con **facilidades accesibles**, participa en nuestra **comunidad** y disfruta de **beneficios exclusivos**. 🎁 Las empresas pueden explorar **nuevas oportunidades** y fomentar un turismo más **inclusivo**. 🌟
        """)

    with col2:
        maps.app()
