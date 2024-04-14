# Importar librerías necesarias.
import streamlit as st
from utils.firebase_utils import login_session

def app():

    # Inicialización de valores.
    if 'ID' not in st.session_state:
        st.session_state['ID'] = ''
    if 'user_type' not in st.session_state:
        st.session_state['user_type'] = ''
    if 'signedout' not in st.session_state:
        st.session_state['signedout'] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False


    # Botón de acción para logout.
    def logout_session():
        st.session_state['signedout'] = False
        st.session_state['signout'] = False
        st.session_state['ID'] = ''
        st.session_state['first_name'] = ''
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
    
    if st.session_state['signout']:
        st.sidebar.title("Bienvenido")
        st.sidebar.markdown(f'**Tipo de usuario**: {st.session_state["user_type"]}')
        st.sidebar.button("Cerrar Sesión", on_click=logout_session)