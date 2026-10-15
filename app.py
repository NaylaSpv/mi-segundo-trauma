import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Análisis estadístico ")
df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)
st.title('Esto es un análisis estadistico de los datos de YARDAS PASOS DATOS TICS')
st.header('Datos de YARDAS PASOS DATOS TICS')
st.dataframe(df.head())

#esta es la estadistica descriptiva de los datos
st.header('Estadística descriptiva de los datos')
st.dataframe(df.describe())


df.columns = [c.lower().replace(' ', '_') for c in df.columns]

#este es el diagrama de caja y bigote de la variable yardas_totales
fig, ax = plt.subplots()
ax.boxplot(df['yardas_totales'])
st.header('Diagrama de caja y bigote de yardas_totales')
st.pyplot(fig)


fig, ax = plt.subplots()
ax.boxplot(df['pases_completos'])
st.header('Diagrama de caja y bigote de pases_completos')
st.pyplot(fig)


col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header('Diagrama de caja y bigote de yardas_totales')
    st.pyplot(fig)
