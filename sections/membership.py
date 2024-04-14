import streamlit as st

def display_rewards_table():
    st.markdown("""
        <style>
        .rewards-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 25px;
        }
        .rewards-table th, .rewards-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .rewards-table th {
            background-color: #3fb0e8;
        }
        .rewards-table tr:hover {
            background-color: #3fb0e8;
        }
        </style>
        <table class="rewards-table">
            <tr>
                <th>Nivel</th>
                <th>Puntos para acumular</th>
                <th>Beneficios</th>
            </tr>
            <tr>
                <td>Aprendiendo a Viajar</td>
                <td>3,000 puntos</td>
                <td>$100 de descuento en restaurantes</td>
            </tr>
            <tr>
                <td>Viajero Junior</td>
                <td>10,000 puntos</td>
                <td>50% de descuento en restaurantes seleccionados<br>Gift card de mes de cumpleaños</td>
            </tr>
            <tr>
                <td>Trotamundos</td>
                <td>15,000 puntos</td>
                <td>70% de descuento en restaurantes y museos seleccionados<br>Gift card de mes de cumpleaños<br>3 actividades culturales gratis</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# Para usar en app.py simplemente llamarías a esta función:
# display_rewards_table()
