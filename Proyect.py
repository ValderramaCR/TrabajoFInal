import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

import streamlit as st

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>Estadísticas de jugadores - Mundial Rusia 2018</h1>", unsafe_allow_html=True)

# Crear dos columnas: una para la imagen y otra para el texto
col1, col2 = st.columns(2)

# En la primera columna, mostrar una imagen con pie de foto
col1.image("Rusia2018.png", caption='El Mundial de Fútbol de Rusia 2018 fue la vigésima primera edición de la Copa del Mundo de la FIFA, celebrada del 14 de junio al 15 de julio de 2018.', width=300)

# Texto para la segunda columna
texto = """
En nuestra página podrás encontrar las estadísticas más completas y detalladas de los jugadores del Mundial de Fútbol de Rusia 2018. Nuestra plataforma te permite explorar y analizar el rendimiento de los futbolistas y de las selecciones que jugaron en esta copa mundial.
"""

# Mostrar el texto en la segunda columna
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# Subtítulo para la experiencia en programación
st.markdown("<h2 style='text-align: center;'>¿Qué Ofrecemos?</h2>", unsafe_allow_html=True)

# Texto sobre la experiencia aprendiendo a programar
texto_2 = """
Estadísticas Detalladas: Accede a datos individuales de cada selección                                                                                           
Comparativas de Selecciones: Compara el rendimiento de tus selecciones favoritas y descubre quiénes destacaron en el torneo.

Análisis y Gráficos: Visualiza las estadísticas a través de gráficos que facilitan la comprensión de los datos.
Únete a Nuestra Comunidad
Participa en nuestras discusiones en redes sociales, comparte tus análisis y forma parte de nuestra comunidad de aficionados al fútbol.
¡Explora, analiza y descubre todo sobre el Mundial Rusia 2018 en nuestra página web!
"""

# Mostrar el texto sobre la experiencia en la aplicación
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# Crear una barra lateral con un título
sidebar = st.sidebar
sidebar.markdown("<h1 style='text-align: center;'>Seleccione la estadística que desea visualiza</h1>", unsafe_allow_html=True)

# Crear una lista de gráficos disponibles
graficos = ['1. Cantidad de jugadores x país', '2. Número de jugadores x posición', '3. Goles anotados x país', '4. Asistencia anotadas x país', '5. Promedio goles x país x partido', '6. Promedio asistencia x país x partido', '7. Goles anotados x posición', '8. Asistencias anotados x posición']

# Cuadro de selección en la barra lateral para elegir un gráfico
grafico_seleccionado = sidebar.selectbox('¡Visualiza las estadísticas del mundial Rusia - 2018 que desees!', graficos)

# Mostrar el gráfico seleccionado en la barra lateral
if grafico_seleccionado == '1. Cantidad de jugadores x país':
    sidebar.image("1. Cantidad de jugadores x país.png", caption='1. Cantidad de jugadores x país', width=500)
elif grafico_seleccionado ==  '2. Número de jugadores x posición':
    sidebar.image("2. Número de jugadores x posición.png", caption='2. Número de jugadores x posición', width=500)
elif grafico_seleccionado == '3. Goles anotados x país':
    sidebar.image("3. Goles anotados x país.png", caption='3. Goles anotados x país', width=500)
elif grafico_seleccionado == '4. Asistencia anotadas x país':
    sidebar.image("4. Asistencia anotadas x país.png", caption='4. Asistencia anotadas x país', width=500)
elif grafico_seleccionado == '5. Promedio goles x país x partido':
    sidebar.image("5. Promedio goles x país x partido.png", caption='5. Promedio goles x país x partido', width=500)
elif grafico_seleccionado == '6. Promedio asistencia x país x partido':
    sidebar.image("6. Promedio asistencia x país x partido.png", caption='6. Promedio asistencia x país x partido', width=500)
elif grafico_seleccionado == '7. Goles anotados x posición':
    sidebar.image("7. Goles anotados x posición.png", caption='7. Goles anotados x posición', width=500)
elif grafico_seleccionado == '8. Asistencias anotados x posición':
    sidebar.image("8. Asistencias anotados x posición.png", caption='8. Asistencias anotados x posición', width=500)