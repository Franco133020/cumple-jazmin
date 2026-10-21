import streamlit as st
import os

# Configurar la página en modo ancho y título
st.set_page_config(
    page_title="Cumple de Jazmín - Panel de Control",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar el menú superior y el pie de página nativo de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Leer el archivo HTML externo
html_file_path = os.path.join(os.path.dirname(__file__), "index.html")
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    st.components.v1.html(html_code, height=1000, scrolling=True)
else:
    st.error("No se encontró el archivo index.html en el repositorio.")
