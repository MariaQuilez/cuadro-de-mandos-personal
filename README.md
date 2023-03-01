# 📈 Cuadro de mandos personal: DATOS SOBRE ALUMNOS EN LA ESCUELA DE IDIOMAS 📊

## Objetivo
Diseño de un cuadro de mandos personal para visualización de datos sobre los alumnos que se han matriculado durante los años 2020 y 2021 en las Escuelas de Idiomas Españolas.

## Los datos
Los datos los he descargado como .csv desde un porta de datos libres de una de las Comunidades Autónomas. Al descargar el archivo, cojo los datos de manera local. Los campos principales que he decidido mostrar son los siguientes: nivel de idioma, idiomas disponibles, provincias, número de alumnos y número de grupos por provincia y de cada idioma.

## Preparación de la aplicación
La aplicación se llama `app.py`. He añadido un `requirements.txt` con las dependencias de mi aplicación, streamlit y pandas.

## Visualización de los datos
He preparado la aplicación para que los datos se muestren en tablas y en gráficos. Para que sea interactivo, he utilizado Altair para mostrar widgets como campos de selección o checbox. Incluso he puesto una barra lateral para uno de los gráficos, el usuario puede decidir los datos que quiere mostrar según el idioma que elija.

## Publicación de la aplicación
Para publicar la aplicación, lo he hecho con Streamlit Cloud. He creado una cuenta y he subido mi aplicación. He creado un repositorio en GitHub y he conectado mi cuenta de Streamlit Cloud con mi cuenta de GitHub. De esta manera, cada vez que hago un push a mi repositorio, se actualiza la aplicación en Streamlit Cloud.

La url de mi aplicación es: https://mariaquilez-cuadro-de-mandos-personal-app-3jnxck.streamlit.app/
