# alumnado matriculado en escuela de idiomas
import pandas as pd
import streamlit as st
import altair as alt

st.title('Datos sobre Alumnado matriculado en Escuela de Idiomas (EOI)')

# carga de datos
DATE_COLUMN = 'date/time'
DATA_URL = ('alumnado_matriculado.csv')


df = pd.read_csv("alumnado_matriculado.csv", sep=";")


# Mostrar un gráfico de barras con el número de alumnos por idioma
st.write("<h2>Número de alumnos matriculados en cada idioma</h2>", unsafe_allow_html=True)
num_alumnos_por_idioma = df.groupby("IDIOMA")["NUM_ALUMNOS"].sum()
st.bar_chart(num_alumnos_por_idioma)

# seleccionar el idioma que se quiere mostrar
st.write("<h2>Número de alumnos y su nivel según idioma </h2>", unsafe_allow_html=True)
st.write("Puedes seleccionar el idioma del que quieres mostrar los datos:", unsafe_allow_html=True)
idiomas = df["IDIOMA"].unique()
selected_idioma = st.selectbox("Selecciona un idioma", idiomas)
df_filtrado = df[df["IDIOMA"] == selected_idioma]
chart_data = df_filtrado.groupby(["COD_NIVEL"])["NUM_ALUMNOS"].sum().reset_index()
chart = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X("COD_NIVEL:O", title="Nivel"),
    y=alt.Y("NUM_ALUMNOS:Q", title="Número de alumnos"),
).properties(width=200, height=200)
st.altair_chart(chart, use_container_width=True)

# tabla de grupos y nalumnos por nivel
st.write("<h2>Tabla con el número de grupos y alumnos según el nivel</h2>", unsafe_allow_html=True)
tabla_data = df_filtrado.groupby(["COD_NIVEL", "DESC_NIVEL"])["NUM_GRUPOS", "NUM_ALUMNOS"].sum().reset_index()
st.write(tabla_data)

# Crear lista desplegable con los idiomas disponibles
idiomas_disponibles = df["IDIOMA"].unique().tolist()
idioma_seleccionado = st.sidebar.selectbox("Selecciona uns idioma", idiomas_disponibles)

# Filtrar los datos según el idioma seleccionado
datos_filtrados = df[df["IDIOMA"] == idioma_seleccionado]

# Generar gráfica
chart = alt.Chart(datos_filtrados).mark_bar().encode(
    x="ANYO_ACADEMICO",
    y="NUM_ALUMNOS"
).properties(
    title=f"Alumnos por año académico en {idioma_seleccionado}"
)

st.altair_chart(chart, use_container_width=True)

st.write("<h2>Gráfica con número de alumnos por provincia según el nivel seleccionado</h2>", unsafe_allow_html=True)

niveles = df["COD_NIVEL"].unique()

# Seleccionar nivel
nivel_seleccionado = st.selectbox("Selecciona un nivel:", niveles)

# Filtrar datos por nivel
data_nivel = df[df["COD_NIVEL"] == nivel_seleccionado]

# Obtener número de alumnos por provincia
num_alumnos_por_provincia = data_nivel.groupby("NOM_PROV")["NUM_ALUMNOS"].sum()


# Mostrar gráfica
st.bar_chart(num_alumnos_por_provincia)

# Obtener la lista de provincias
provincias = df["NOM_PROV"].unique()

# Preguntar al usuario la provincia que desea visualizar
provincia_seleccionada = st.radio("Selecciona una provincia", provincias)

# Filtrar los datos por la provincia seleccionada
df_provincia = df[df["NOM_PROV"] == provincia_seleccionada]

# Agrupar por idioma y obtener el número de alumnos
df_num_alumnos = df_provincia.groupby("IDIOMA")["NUM_ALUMNOS"].sum().reset_index()

# Crear un gráfico de barras con Altair
bar_chart = alt.Chart(df_num_alumnos).mark_bar().encode(
    x=alt.X("NUM_ALUMNOS:Q", title="Número de alumnos"),
    y=alt.Y("IDIOMA:N", title="Idioma"),
    tooltip=["IDIOMA", "NUM_ALUMNOS"]
).properties(width=500, height=400, title=f"Número de alumnos por idioma en {provincia_seleccionada}")

pd.set_option("display.max_colwidth", None)

# Mostrar el gráfico
st.altair_chart(bar_chart)

