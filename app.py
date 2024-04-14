# Importar las librerías necesarias.
import streamlit as st
from st_pages import Page, show_pages, hide_pages
from sections import login, maps
from utils.firebase import Firebase


def bussines_register():
    st.title("Business Registration 🏢")
    email = st.text_input('📧 Email Address')
    password = st.text_input('🔒 Password', type='password')
    name = st.text_input('🏢 Business Name')
    bss_type = st.selectbox('📊 Business Type', ['Food 🍔', 'Culture 🎭', 'Entertainment 🎮'])
    submit = st.button("Create Business")

    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        auth = Firebase().getauth()
        user = auth.create_user_with_email_and_password(email, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('email').set(email)
        db.child(user['localId']).child('password').set(password)
        db.child(user['localId']).child('user_type').set('bussines')
        db.child(user['localId']).child('name').set(name)
        db.child(user['localId']).child('bss_type').set(bss_type)
        st.success('La cuenta ha sido creada correctamente.')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        bss_type = ''


def user_register():
    st.title("Registro de Usuarios")
    email = st.text_input('Correo Electrónico')
    password = st.text_input('Contraseña', type='password')
    name = st.text_input('Nombre')
    last_name = st.text_input("Apellidos")
    submit = st.button("Crear Usuario")
    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        auth = Firebase().getauth()
        user = auth.create_user_with_email_and_password(email, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('email').set(email)
        db.child(user['localId']).child('password').set(password)
        db.child(user['localId']).child('user_type').set('client')
        db.child(user['localId']).child('name').set(name)
        db.child(user['localId']).child('last_name').set(last_name)
        st.success('La cuenta ha sido creada correctamente.')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        last_name = ''


def register():
    st.title("Registrate")
    selected_option = st.radio("¿Qué tipo de usuario eres?", ("Cliente", "Empresa"))
    if selected_option == 'Cliente':
        user_register()
    else:
        bussines_register()


def home():
    st.title("Hidden Places")
    maps.app()




# Configuración de Streamlit.
st.set_page_config(
    page_title="Hidden Places | Home",
    page_icon="🗺️",
    initial_sidebar_state="expanded",
)

# Iniciar Sesión.
login.app()

# Si hay usuario.
if st.session_state['user_type'] != '':
    pass
else:
    if "selection" not in st.session_state:
        home()
        if st.button("Registrar"):
            st.session_state.selection = "REGISTRAR"
    elif st.session_state.selection == "REGISTRAR":
        register()
