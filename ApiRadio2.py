import streamlit as st 
import pandas as pd 
import requests 
import matplotlib.pyplot as plt 
 
# Consulta a la API para obtener los datos 
url = "https://radioid.net/api/dmr/user/?country=Chile" 
response = requests.get(url) 
 
# Verificar si la respuesta fue exitosa 
if response.status_code == 200: 
     data = response.json() 
     df = pd.DataFrame(data['results']) # Convertir los datos JSON en un DataFrame 
else: 
    st.error("Error en la consulta de datos") 
 
# Barra lateral 
st.sidebar.header("Opciones de Filtro") 
st.sidebar.write("### Configuración de Visualización") 
 
# Agregar cuadros de texto o instrucciones 
st.write("Esta aplicación muestra información en tiempo real de los radioaficionados en Chile registrados para comunicación digital.") 
st.write(df) 
 
# Botón para cargar datos 
if st.sidebar.button("Cargar Datos"): 
    st.write("Los datos han sido cargados y actualizados.") 
 
# Ejemplo de filtro por categoría o tipo de usuario (ajusta según los datos disponibles) 
categoria = st.sidebar.selectbox("Selecciona una Región", df['state'].unique()) 
df_filtrado = df[df['state'] == categoria] 
 
# Botón de actualización 
if st.sidebar.button("Actualizar Datos"): 
    # Código para refrescar o procesar los datos según filtros 
     st.write("Datos actualizados") 
 
# Mostrar DataFrame filtrado 
st.write("### Datos de Radioaficionados en Chile Según Región") 
st.write(df_filtrado) 
 
# Gráfico de barras (por ejemplo, cantidad de usuarios por región) 
fig, ax = plt.subplots() 
df['state'].value_counts().plot(kind='bar', ax=ax) 
ax.set_title("Cantidad de Usuarios por Región") 
ax.set_xlabel("Región") 
ax.set_ylabel("Cantidad") 
st.pyplot(fig) 
 
# Gráfico de torta (por ejemplo, distribución de categorías de usuarios) 
fig, ax = plt.subplots() 
df['state'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax) 
ax.set_title("Distribución por Región de Usuario") 
st.pyplot(fig) 
