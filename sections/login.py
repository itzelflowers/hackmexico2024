# Importar librerías necesarias.
import streamlit as st
from utils.firebase_utils import login_session
# Conexión a base de datos.
from utils.firebase import Firebase
from sections import register_places, home, see_places
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
from sections.membership import display_rewards_table

# Acceso a Firebase.
db = Firebase().getdb()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

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
    
    button_css = """
    <style>
    div.stButton > button:first-child {
        background-color: #f97316;  /* Color naranja para contraste */
        color: #ffffff;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #fb923c;  /* Color más claro para el hover */
        border: none;
    }
    </style>
    """
    
    st.markdown(button_css, unsafe_allow_html=True)

    # Información de login.
    if not st.session_state['signedout']:
        st.sidebar.image('img\logoconnombre.png', use_column_width=True, width=180)
        st.sidebar.title("Inicio de Sesión") 
        st.sidebar.write("Inicia Sesión para ver más características")
        text_email = st.sidebar.text_input('Correo Electrónico', key='email')
        text_password = st.sidebar.text_input('Contraseña', type='password', key='password')
        # Enviar información.
        st.sidebar.button("Iniciar Sesión", on_click=login_session, args=(text_email, text_password))
        lottie_intro = load_lottiefile("img\\similo3.json")

        # Mostrar la animación Lottie en la barra lateral
        with st.sidebar:
            st_lottie(lottie_intro)   

    # Sesión Iniciada.
    if st.session_state['signout']:
        lottie_intro = load_lottiefile("img\\similo3.json") 
        # st_lottie(lottie_intro)
        st.sidebar.image('img\logoconnombre.png', use_column_width=True, width=180)
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
            if st.sidebar.button("Recompensas"):
                display_rewards_table()
            if st.sidebar.button("Inicio"):
                st.session_state.selection = "HOME"
            if st.sidebar.button("Sectores"):
                st.session_state.selection = "SECTORES"
            if st.sidebar.button("Recomendaciones"):
                st.session_state.selection = "RECOMENDACIONES"
            if st.sidebar.button("Pefil"):
                st.session_state.selection = "PERFIL"
            # Options.
            if "selection" not in st.session_state:
                user_home.app()
            elif st.session_state.selection == "REGISTRAR":
                user_home.app()
            elif st.session_state.selection == "HOME":
                user_home.app()
            elif st.session_state.selection == "VER_LUGARES":
                see_places.app()
        st.sidebar.button("Cerrar Sesión", on_click=logout_session)

        with st.sidebar:
            st_lottie(lottie_intro) 