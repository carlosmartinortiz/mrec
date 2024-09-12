import pandas as pd
import schedule
import time
from datetime import datetime
import streamlit as st
from streamlit_js_eval import streamlit_js_eval

# Inicializar contadores en session_state para mantener el estado
if 'solicitudes_recomendacion' not in st.session_state:
    st.session_state['solicitudes_recomendacion'] = 10

if 'recomendaciones_enviadas' not in st.session_state:
    st.session_state['recomendaciones_enviadas'] = 0

# Contenedor vacío para la sección de datos que se actualizarán
revisar_contenedor = st.empty()

def actualizar_contenido():
    # Obtener la fecha y hora actuales
    now = datetime.now()
    fecha_ultima_revision = now.strftime('Día :%d-%m-%Y, Hora: %H:%M:%S')
    
    # Actualizar solo el contenido de la sección con datos
    with revisar_contenedor:
        st.caption("En revisión " + "(" + fecha_ultima_revision + "): " + str(st.session_state['solicitudes_recomendacion']))

# Título de la aplicación (solo se dibuja una vez)
st.title("Movie Recommendation Engine - Monitor")

# Programar el trabajo con Schedule
def job_with_argument(name):
    # Actualizar los contadores o realizar otras operaciones
    st.session_state['solicitudes_recomendacion'] += 1
    actualizar_contenido()

# Programar la ejecución del trabajo cada cierto tiempo
schedule.every(5).seconds.do(job_with_argument, "Job1")

# Ejecutar el loop de Schedule
while True:
    schedule.run_pending()
    time.sleep(1)
