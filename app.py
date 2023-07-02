import streamlit as st
import requests
import pandas as pd
from cachetools import cached, TTLCache

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Datos Abiertos Gobierno de España") 

SPARQL_ENDPOINT = "http://datos.gob.es/virtuoso/sparql"
cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def get_dataset_names(sparql_endpoint):
    query = """
    SELECT ?dataset ?title
    WHERE {
      ?dataset a <http://www.w3.org/ns/dcat#Dataset> .
      ?dataset <http://purl.org/dc/terms/title> ?title .
    }
    LIMIT 100
    """
    response = requests.get(sparql_endpoint, params={"query": query, "format": "application/sparql-results+json"})
    if response.status_code == 200:
        results = response.json()
        data = [(result['dataset']['value'], result['title']['value']) for result in results["results"]["bindings"]]
        return pd.DataFrame(data, columns=['Dataset', 'Title'])
    else:
        return None

@cached(cache)
def get_sparql_data(query, sparql_endpoint):
    response = requests.get(sparql_endpoint, params={"query": query, "format": "application/sparql-results+json"})
    if response.status_code == 200:
        results = response.json()
        keys = results["head"]["vars"]
        data = [
            {key: result[key]["value"] for key in keys}
            for result in results["results"]["bindings"]
        ]
        return pd.DataFrame(data)
    else:
        return None

st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeydeV4N1I4-65fUz_ETGPI9LaQ-Ejxri1OLCsWOIumr_kxXcbCWZicNEo4BW3du2IGw&usqp=CAU", use_column_width=True) 
st.sidebar.title("Navegador de Datasets")
st.sidebar.subheader("Opciones de navegación")
option = st.sidebar.radio("Selecciona una opción:", ("Lista de Datasets", "Consulta SPARQL Personalizada"))

if option == "Lista de Datasets":
    st.title("Lista de Datasets")
    st.markdown("---")

    dataset_names = get_dataset_names(SPARQL_ENDPOINT)
    if dataset_names is not None and not dataset_names.empty:
        st.table(dataset_names)
    else:
        st.warning("No se pudieron obtener los nombres de los datasets.")
    
elif option == "Consulta SPARQL Personalizada":
    st.title("Consulta de Datasets")
    st.markdown("---")

    example_query = """PREFIX dcat: <http://www.w3.org/ns/dcat#>
    SELECT ?distribution
    WHERE {
      <https://datos.gob.es/catalogo/ea0010587-tasas-de-inmigracion-procedente-del-extranjero-segun-sexo-edad-y-ano-identificador-api-36758> dcat:distribution ?distribution .
    }"""
    st.markdown("### Ejemplo de consulta:")
    st.code(example_query, language='sparql')
    user_query = st.text_area("Introduce tu consulta SPARQL aquí:", value="", height=200)

    if st.button("Ejecutar consulta"):
        if user_query:
            df = get_sparql_data(user_query, SPARQL_ENDPOINT)
            if df is not None and not df.empty:
                st.table(df)
            else:
                st.warning("No se obtuvieron resultados o hubo un error en la consulta.")
        else:
            st.warning("Por favor, introduce una consulta SPARQL válida.")

