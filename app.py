import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Cumple de Jazmín - Panel de Control",
    page_icon="🎉",
    layout="wide"
)

# Estilos CSS personalizados para mantener la estética original
st.markdown("""
<style>
    .main-header {
        font-size: 1.8rem;
        color: #e91e63;
        font-weight: bold;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Pantalla de acceso privado (Contraseña)
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("## 🔒 Acceso Privado")
    st.markdown("Ingresa la contraseña para ver la organización del cumple de Jazmín.")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Ingresar", type="primary"):
        if password == "Jazmin2024":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta. Intenta de nuevo.")
    st.stop()

# --- PANEL DE CONTROL PRINCIPAL ---
st.markdown('<p class="main-header">🎉 Cumple de Jazmín - Panel de Control</p>', unsafe_allow_html=True)
st.write("Panel de Control de Invitaciones y Organización")

# Pestañas principales
tab_invitados, tab_video, tab_organizacion, tab_compras, tab_cronograma = st.tabs([
    "📑 Invitados", 
    "🎬 Invitación / Video", 
    "📦 Organización", 
    "🛒 Compras", 
    "⏱️ Cronograma"
])

with tab_invitados:
    st.subheader("Gestión de Invitados")
    
    # Métricas rápidas de ejemplo
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Invitados", value="146")
    with col2:
        st.metric(label="Confirmados", value="4")
    with col3:
        st.metric(label="Falta Confirmar", value="142")
    with col4:
        st.metric(label="No podrán asistir", value="0")

    search_query = st.text_input("🔍 Buscar nombre o celular...")
    
    # Vista previa de la lista inicial de invitados
    st.markdown("### Listado")
    invitados_ejemplo = [
        {"N°": 1, "Nombre": "Ines Garcia", "Celular": "3885191848", "Tipo": "ADULTO/A", "Estado": "CONFIRMADO"},
        {"N°": 2, "Nombre": "Juan Jose Jacinto", "Celular": "3883503008", "Tipo": "ADULTO/A", "Estado": "CONFIRMADO"},
        {"N°": 3, "Nombre": "Lucas Joaquin Jacinto", "Celular": "3886110139", "Tipo": "NENE", "Estado": "CONFIRMADO"},
        {"N°": 4, "Nombre": "Facundo Agustin Jacinto", "Celular": "3884660542", "Tipo": "NENE", "Estado": "CONFIRMADO"},
    ]
    st.dataframe(invitados_ejemplo, use_container_width=True)

with tab_video:
    st.subheader("🎬 Video de la Invitación del Cumple de Jazmín")
    st.info("Puedes reproducir o verificar el archivo de video de la invitación aquí.")
    # Si tienes el archivo de video subido al repositorio, puedes referenciarlo:
    try:
        st.video("WhatsApp Video 2026-10-07 at 15.41.41.mp4")
    except Exception:
        st.warning("El archivo de video no se encuentra en el repositorio.")

with tab_organizacion:
    st.subheader("📦 Tareas y Logística")
    col_A, col_B = st.columns(2)
    with col_A:
        st.markdown("**🎈 Decoración**")
        st.checkbox("Centro de mesa", value=False)
        st.checkbox("Banner principal (4m x 1,80m)", value=False)
        st.checkbox("Banner de ingreso (1,80m x 90cm)", value=False)
        st.checkbox("Globos para el arco", value=False)
    with col_B:
        st.markdown("**🪑 Equipamiento y Local**")
        st.checkbox("Parlantes", value=False)
        st.checkbox("Alargador para enchufar", value=False)
        st.checkbox("Escalera para bolsitas", value=False)

with tab_compras:
    st.subheader("🛒 Lista de Compras")
    st.checkbox("🥩 Pollo y Carne (Carnicería)", value=False)
    st.checkbox("🍞 Pan de miga y prepizzas (Panadería)", value=False)
    st.checkbox("🍬 Golosinas para bolsitas y candy bar", value=False)
    st.checkbox("🧂 Harina, dulce de leche, margarina", value=False)

with tab_cronograma:
    st.subheader("⏱️ Cronograma del Evento (17/10/2026)")
    cronograma_data = [
        {"Horario": "14:00 - 15:00", "Actividad": "Llegada e Instalación", "Notas": "Montaje de peloteros y mesa principal."},
        {"Horario": "15:00 - 15:30", "Actividad": "Inicio & Recepción", "Notas": "Llegada de invitados."},
        {"Horario": "15:30 - 16:30", "Actividad": "Payasa - Bloque 1", "Notas": "Juegos integradores."},
        {"Horario": "18:45 - 19:15", "Actividad": "Torta & Cumpleaños", "Notas": "Cantar el feliz cumpleaños."}
    ]
    st.table(cronograma_data)
