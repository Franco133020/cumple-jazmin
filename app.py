import streamlit as st
import streamlit.components.v1 as components

# Configurar la página para que ocupe todo el ancho
st.set_page_config(page_title="Cumple de Jazmín", page_icon="🎉", layout="wide")

# Leer y renderizar el archivo index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Mostrar la aplicación web dentro de Streamlit con altura ajustable
components.html(html_code, height=900, scrolling=True)
