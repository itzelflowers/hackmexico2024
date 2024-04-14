# Importar librerías necesarias.
# Web.
import streamlit as st
from streamlit_folium import st_folium
# Data.
import geopandas
from shapely.geometry import LineString
import folium


# Shapefile CDMX.
lineas_cdmx = geopandas.read_file(('./shapefiles/poligonos_alcaldias_cdmx/poligonos_alcaldias_cdmx.shp'))
lineas_cdmx['centroide'] = lineas_cdmx.centroid


# Diccionario.
alcaldias = {
    '09002': 'Azcapotzalco',
    '09003': 'Coyoacán',
    '09004': 'Cuajimalpa de Morelos',
    '09005': 'Gustavo A. Madero',
    '09006': 'Iztacalco',
    '09007': 'Iztapalapa',
    '09008': 'La Magadalena Contreras',
    '09009': 'Milpa Alta',
    '09010': 'Álvaro Obregón',
    '09011': 'Tláhuac',
    '09012': 'Tlalpan',
    '09013': 'Xochimilco',
    '09014': 'Benito Juárez',
    '09015': 'Cuauhtémoc',
    '09016': 'Miguel Hidalgo',
    '09017': 'Venustiano Carranza'
}


# Inicalización de mapa.
def init_map(center=(19.4325019109759, -99.1322510732777), zoom_start=10, map_type="cartodbpositron"):
    return folium.Map(location=center, zoom_start=zoom_start, tiles=map_type)


# Plotear mapa
def plot_map(folium_map):
    for idx, row in lineas_cdmx.iterrows():
        folium.GeoJson(row.geometry,
                        style_function=lambda x: {'fillColor': '#FF0000', 'color': '#000000', 'weight': 1.5, 'fillOpacity': 0.5},
                        tooltip=alcaldias[row['CVEGEO']]).add_to(folium_map)
        folium.Marker(location=[row.centroide.y, row.centroide.x], tooltip=alcaldias[row['CVEGEO']]).add_to(folium_map)
    return folium_map

def app():
    m = init_map()
    m = plot_map(m)
    folium_map = st_folium(m, width=700, height=500)  # Ajusta el tamaño del mapa según sea necesario
    st.session_state.selected_id = folium_map['last_object_clicked_tooltip']
    if st.session_state.selected_id is not None:
        st.subheader(f'{st.session_state.selected_id}')