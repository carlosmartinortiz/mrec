# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NkVceasbsElMtZk3JANXxcSh7Q4PveT-
"""

#!pip install -q -U streamlit
#!pip install -q -U schedule

import pandas as pd
import schedule
import time
from datetime import datetime

import streamlit as st

def job_with_argument(name):
    now = datetime.now()
    fecha_ultima_revision = now.strftime('Día :%d-%m-%Y, Hora: %H:%M:%S')
    # Título de la aplicación
    st.title("Movie Recommendation Engine - Monitor (" + fecha_ultima_revision + ")")

    #print(f"{name}: {fecha_ultima_revision}")
    #Leer el archivo MOVIERECOMMENDATION desde la última línea leída con anterioridad
    #Call API VICTORización (dentro escribe salida a excel JUAN: https://docs.google.com/spreadsheets/d/1T2H33PS-I0g0PhQyYblMrYcc8K3FSLbEkonV0VDYfwI/edit?gid=0#gid=0)
    #Guardar en un archivo en que línea del excel MOVIERECOMMENDATION quedó:
    #Escribir Cuántos llegaron (Pantalla Streamlit)
    #Call API Mailing

schedule.every(10).seconds.do(job_with_argument, name="MovieRec")

# Contadores iniciales
solicitudes_recomendacion = 0
recomendaciones_enviadas = 0

# Crear un contenedor de solicitudes de recomendación
with st.container():
    #st.header("Solicitudes de Recomendación")
    # Crear una caja de texto para las solicitudes de recomendación
    st.image("https://cdn.icon-icons.com/icons2/491/PNG/512/email-inbox_48097.png", caption="Total de Solicitudes de Recomendación pendientes de revisar", width=200)
    solicitudes_recomendacion = st.text_input("En revisión:", value=str(solicitudes_recomendacion),max_chars=9)

# Crear un contenedor de recomendaciones enviadas
with st.container():
    #st.header("Recomendaciones Enviadas")
    # Crear una caja de texto para las recomendaciones enviadas
    st.image("https://img.freepik.com/vector-gratis/enviar-concepto-correo-electronico_24908-60321.jpg?w=740&t=st=1726111970~exp=1726112570~hmac=3cb83788ddf6b7263132dd50cbfb760f3ba79c9d2707e51041a8b5e4e2f35861", caption="Total de Recomendaciones respondidas recientemente", width=200)
    recomendaciones_enviadas = st.text_input("Respondidas:", value=str(recomendaciones_enviadas),max_chars=9)


# Lógica para actualizar los contadores según sea necesario
# Aquí puedes agregar la lógica para manejar las solicitudes y recomendaciones

while True:
    schedule.run_pending()
    time.sleep(1)