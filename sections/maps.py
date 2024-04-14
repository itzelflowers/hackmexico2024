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
    folium_map = st_folium(m, width=500, height=500)  # Ajusta el tamaño del mapa según sea necesario
    st.session_state.selected_id = folium_map['last_object_clicked_tooltip']
    if st.session_state.selected_id is not None:
        st.subheader(f'{st.session_state.selected_id}')
        lugares = db.child('Lugares').get().val()
        for l in lugares:
            lugar = db.child('Lugares').child(l).child('Location').get().val()
            if st.session_state.selected_id == lugar:
                location = db.child('Lugares').child(l).child('Location').get().val()
                bss_type = db.child('Lugares').child(l).child('bss_type').get().val()
                asistencia = db.child('Lugares').child(l).child('asistencia').get().val()
                elevadores = db.child('Lugares').child(l).child('elevadores').get().val()
                estacionamiento = db.child('Lugares').child(l).child('estacionamiento').get().val()
                rampas = db.child('Lugares').child(l).child('rampas').get().val()
                sillas_ruedas = db.child('Lugares').child(l).child('sillas_ruedas').get().val()
                st.subheader(l)
                st.write(f'Alcaldía: {location}')
                st.write(f'Tipo de negocio: {bss_type}')
                st.write(f'asistencia: {asistencia}')
                st.write(f'elevadores: {elevadores}')
                st.write(f'estacionamiento: {estacionamiento}')
                st.write(f'rampas: {rampas}')
                st.write(f'sillas_ruedas: {sillas_ruedas}')

#
#import streamlit as st
#from streamlit_folium import st_folium
#import geopandas
#import folium
#from utils.firebase import Firebase
#
#def maps_app():
#    db = Firebase().getdb()
#    
#    # Shapefile CDMX.
#    lineas_cdmx = geopandas.read_file(('./shapefiles/poligonos_alcaldias_cdmx/poligonos_alcaldias_cdmx.shp'))
#    lineas_cdmx['centroide'] = lineas_cdmx.centroid
#
#    # Diccionario de alcaldías.
#    alcaldias = {
#    '09002': 'Azcapotzalco',
#    '09003': 'Coyoacán',
#    '09004': 'Cuajimalpa de Morelos',
#    '09005': 'Gustavo A. Madero',
#    '09006': 'Iztacalco',
#    '09007': 'Iztapalapa',
#    '09008': 'La Magadalena Contreras',
#    '09009': 'Milpa Alta',
#    '09010': 'Álvaro Obregón',
#    '09011': 'Tláhuac',
#    '09012': 'Tlalpan',
#    '09013': 'Xochimilco',
#    '09014': 'Benito Juárez',
#    '09015': 'Cuauhtémoc',
#    '09016': 'Miguel Hidalgo',
#    '09017': 'Venustiano Carranza'
#}
#
#    # Inicialización del mapa.
#    def init_map(center=(19.4325019109759, -99.1322510732777), zoom_start=10, map_type="cartodbpositron"):
#        return folium.Map(location=center, zoom_start=zoom_start, tiles=map_type)
#
#    # Función para plotear el mapa.
#    def plot_map(folium_map):
#        for idx, row in lineas_cdmx.iterrows():
#            folium.GeoJson(row.geometry,
#                        style_function=lambda x: {'fillColor': '#FF0000', 'color': '#000000', 'weight': 1.5, 'fillOpacity': 0.5},
#                        tooltip=alcaldias[row['CVEGEO']]).add_to(folium_map)
#            folium.Marker(location=[row.centroide.y, row.centroide.x], tooltip=alcaldias[row['CVEGEO']]).add_to(folium_map)
#        return folium_map
#
#    # Crear y plotear el mapa.
#    def app():
#        m = init_map()
#        m = plot_map(m)
#        folium_map = st_folium(m, width=700, height=500)  # Ajusta el tamaño del mapa según sea necesario
#        st.session_state.selected_id = folium_map['last_object_clicked_tooltip']
#        if st.session_state.selected_id is not None:
#            st.subheader(f'{st.session_state.selected_id}')
#            lugares = db.child('Lugares').get().val()
#            for l in lugares:
#                lugar = db.child('Lugares').child(l).child('Location').get().val()
#                if st.session_state.selected_id == lugar:
#                    location = db.child('Lugares').child(l).child('Location').get().val()
#                    bss_type = db.child('Lugares').child(l).child('bss_type').get().val()
#                    asistencia = db.child('Lugares').child(l).child('asistencia').get().val()
#                    elevadores = db.child('Lugares').child(l).child('elevadores').get().val()
#                    estacionamiento = db.child('Lugares').child(l).child('estacionamiento').get().val()
#                    rampas = db.child('Lugares').child(l).child('rampas').get().val()
#                    sillas_ruedas = db.child('Lugares').child(l).child('sillas_ruedas').get().val()
#                    st.subheader(l)
#                    st.write(f'Alcaldía: {location}')
#                    st.write(f'Tipo de negocio: {bss_type}')
#                    st.write(f'asistencia: {asistencia}')
#                    st.write(f'asistencia: {elevadores}')
#                    st.write(f'asistencia: {estacionamiento}')
#                    st.write(f'asistencia: {rampas}')
#                    st.write(f'asistencia: {sillas_ruedas}')
#
## Para usar esta función de mapa en la aplicación principal:
## maps_app()
#