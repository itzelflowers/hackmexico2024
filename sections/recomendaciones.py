# Importar librerías necesarias.
# Web.
import streamlit as st
from streamlit_folium import st_folium
# Data.
import geopandas
from shapely.geometry import LineString
import folium
from utils.firebase import Firebase

db = Firebase().getdb()

def app():
    st.title("Tus recomendaciones")
    st.write("De acuerdo a tus necesidades y a las facilidades que ofrecen los lugares. Tenemos las siguientes recomendaciones.")
    lugares = db.child('Lugares').get().val()
    for l in lugares:
        st.subheader(l)