# Navegador de Datasets de Datos Abiertos del Gobierno de España

Este proyecto es una aplicación web para explorar y consultar los datasets disponibles en el portal de datos abiertos del Gobierno de España.

![Imagen de la Aplicación](https://datos.gob.es/sites/default/files/logo_0.svg)

## Demo en Vivo

Puedes ver una versión en vivo de la aplicación en el siguiente enlace:

[Ver Demo](https://datosabiertos.streamlit.app/)

## Características

- **Lista de Datasets**: La aplicación muestra una lista de datasets disponibles en el portal.
- **Consulta SPARQL Personalizada**: Permite al usuario introducir y ejecutar consultas SPARQL personalizadas para obtener información específica de los datasets.
- **Caché de Datos**: Utiliza un caché para mejorar el rendimiento de las consultas y reducir la carga en el servidor SPARQL.

## Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework de Python para crear aplicaciones web de análisis de datos. Se utiliza para diseñar y desplegar la interfaz de la aplicación.
- **[Pandas](https://pandas.pydata.org/)**: Biblioteca de Python para manipulación y análisis de datos. Se utiliza para procesar los datos obtenidos a través de las consultas SPARQL.
- **[Requests](https://docs.python-requests.org/en/master/)**: Biblioteca de Python para realizar solicitudes HTTP. Se utiliza para comunicarse con el endpoint SPARQL.
- **[CacheTools](https://cachetools.readthedocs.io/)**: Biblioteca de Python para caché. Se utiliza para almacenar en caché las consultas y mejorar el rendimiento de la aplicación.
- **SPARQL**: Lenguaje de consulta utilizado para consultar los datasets disponibles en el portal de datos abiertos del Gobierno de España.

## ¿Para Qué Sirve?

Esta aplicación es útil para personas interesadas en explorar y trabajar con datos abiertos proporcionados por el Gobierno de España. Permite obtener una visión general de los datasets disponibles y realizar consultas personalizadas para extraer datos específicos.

## Cómo Usarlo

1. Clonar este repositorio o descargarlo como ZIP.
2. Instalar las dependencias necesarias con `pip install -r requirements.txt`.
3. Ejecutar la aplicación con el comando `streamlit run nombre_de_tu_archivo.py`.
4. Navega a la URL que Streamlit te proporciona (por lo general, http://localhost:8501) y explora la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna mejora o corrección, por favor, crea un 'pull request' o abre un 'issue'.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

 
