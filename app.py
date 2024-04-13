# Importar las librerías necesarias.
import streamlit as st
from utils.firebase import Firebase
import pyrebase

config = {
    'apiKey': "AIzaSyCGw0yokHwaEgWWNc1OGDo-8Iwk8_p5R6Q",
    'authDomain': "hackmexico2-784a3.firebaseapp.com",
    'databaseURL': "https://hackmexico2-784a3-default-rtdb.firebaseio.com",
    'projectId': "hackmexico2-784a3",
    'storageBucket': "hackmexico2-784a3.appspot.com",
    'messagingSenderId': "499824700976",
    'appId': "1:499824700976:web:75ce309870353aa99c07f5",
    'measurementId': "G-E3R7BYY22N"
}


# Configuración de Streamlit.
st.set_page_config(
    page_title="Hidden Places | Registro",
    page_icon="🗺️",
    initial_sidebar_state="expanded",
)

def bussines_register():
    st.title("Registro de Empresas")
    email = st.text_input('Correo Electrónico')
    password = st.text_input('Contraseña', type='password')
    name = st.text_input('Nombre Empresa')
    bss_type = st.selectbox('Tipo de Empresa', ['Comida', 'Cultura', 'Entretenimiento'])
    submit = st.button("Crear Empresa")
    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        auth = Firebase().getauth()
        user = auth.create_user_with_email_and_password(email, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('email').set(email)
        db.child(user['localId']).child('password').set(password)
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
    bss_type = st.checkbox()
    submit = st.button("Crear Empresa")
    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        auth = Firebase().getauth()
        user = auth.create_user_with_email_and_password(email, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('email').set(email)
        db.child(user['localId']).child('password').set(password)
        db.child(user['localId']).child('name').set(name)
        db.child(user['localId']).child('bss_type').set(bss_type)
        st.success('La cuenta ha sido creada correctamente.')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        bss_type = ''


bussines_register()