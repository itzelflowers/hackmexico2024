# Importar librerías necesarias.
import streamlit as st
from utils.firebase_utils import login_session
# Conexión a base de datos.
from utils.firebase import Firebase
from sections import register_places, home, see_places

# Acceso a Firebase.
db = Firebase().getdb()

def app():

    # Inicialización de valores.
    if 'ID' not in st.session_state:
        st.session_state['ID'] = ''
    if 'user_type' not in st.session_state:
        st.session_state['user_type'] = ''
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if 'bss_type' not in st.session_state:
        st.session_state['bss_type'] = ''
    if 'last_name' not in st.session_state:
        st.session_state['last_name'] = ''
    if 'signedout' not in st.session_state:
        st.session_state['signedout'] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False


    # Botón de acción para logout.
    def logout_session():
        st.session_state['signedout'] = False
        st.session_state['signout'] = False
        st.session_state['ID'] = ''
        if st.session_state['user_type'] == 'bussines':
            st.session_state['name'] = ''
            st.session_state['bss_type'] = ''
        else:
            st.session_state['name'] = ''
            st.session_state['last_name'] = ''
        st.session_state['user_type'] = ''
    

    # Información de login.
    if not st.session_state['signedout']:
        st.sidebar.title("Inicio de Sesión") 
        st.sidebar.write("Inicia Sesión para ver más características")
        text_email = st.sidebar.text_input('Correo Electrónico', key='email')
        text_password = st.sidebar.text_input('Contraseña', type='password', key='password')
        # Enviar información.
        st.sidebar.button("Iniciar Sesión", on_click=login_session, args=(text_email, text_password))
    

    # Sesión Iniciada.
    if st.session_state['signout']:
        st.sidebar.title("Bienvenido")
        if st.session_state['user_type'] == 'bussines':
            st.session_state['name'] = db.child(st.session_state.ID).child('name').get().val()
            st.session_state['bss_type'] = db.child(st.session_state.ID).child('bss_type').get().val()
            st.sidebar.subheader(f'{st.session_state["name"]}')
            st.sidebar.markdown(f'**Giro de la empresa**: {st.session_state["bss_type"]}')
            if st.sidebar.button("Registrar Lugar"):
                st.session_state.selection = "LUGARES"
            if st.sidebar.button("Ver Lugares"):
                st.session_state.selection = "VER_LUGARES"
            # Options.
            if "selection" not in st.session_state:
                register_places.app()
            elif st.session_state.selection == "REGISTRAR":
                register_places.app()
            elif st.session_state.selection == "LUGARES":
                register_places.app()
            elif st.session_state.selection == "VER_LUGARES":
                see_places.app()
        else:
            st.session_state['name'] = db.child(st.session_state.ID).child('name').get().val()
            st.session_state['last_name'] = db.child(st.session_state.ID).child('last_name').get().val()
            st.sidebar.subheader(f'{st.session_state["name"]} {st.session_state["last_name"]}')
            if st.sidebar.button("Inicio"):
                st.session_state.selection = "LUGARES"
            if st.sidebar.button("Sectores"):
                st.session_state.selection = "EVENTOS"
            if st.sidebar.button("Recomendaciones"):
                st.session_state.selection = "VER_LUGARES"
            if st.sidebar.button("Pefil"):
                st.session_state.selection = "VER_EVENTOS"
        st.sidebar.button("Cerrar Sesión", on_click=logout_session)