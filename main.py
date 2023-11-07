import seaborn as sns
import pandas as pd
import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt
from lib import personalised_graphics

# Importar y transformar sig data
sig_provincias = gpd.read_file("data/sig/provincia.shp")
sig_localidades = gpd.read_file("data/sig/localidad_bahra.shp")
sig_provincias["nam"] = sig_provincias["nam"].str.replace("Ciudad Autónoma de Buenos Aires", "Capital Federal")
sig_provincias["nam"] = sig_provincias["nam"].str.replace("Tierra del Fuego, Antártida e Islas del Atlántico Sur", "Tierra Del Fuego")
sig_provincias["nam"] = sig_provincias["nam"].str.replace("Santiago del Estero", "Santiago Del Estero")
sig_provincias.drop(columns=["gid", "entidad", "fna", "gna", "in1", "fdc", "sag"], inplace=True)
sig_provincias.rename(columns={"nam": "Provincia"}, inplace=True)

accesos_prov_por_tecnologia = pd.read_csv("data/unprocessed/Internet_Accesos-por-tecnologia (1).csv")


st.set_page_config(layout="wide")

st.sidebar.markdown("<h4 style='text-align: left;'>Filters:</h4>", unsafe_allow_html=True)
selected_year = st.sidebar.slider('Rango temporal:', min_value=2014, max_value=2022)
st.sidebar.markdown("<h5 style='text-align: left;'> </h5>", unsafe_allow_html=True) # Spacing
selected_state = st.sidebar.multiselect('Provincia', ["Buenos Aires","Catamarca","San Juan"])
st.sidebar.markdown("<h5 style='text-align: left;'> </h5>", unsafe_allow_html=True) # Spacing
selected_state = st.sidebar.multiselect('Tecnologia', ["Buenos Aires","Catamarca","San Juan"])
st.sidebar.markdown("<h5 style='text-align: left;'> </h5>", unsafe_allow_html=True) # Spacing
selected_state = st.sidebar.multiselect('Velocidad', ["Buenos Aires","Catamarca","San Juan"])

st.markdown("<h5 style='text-align: left;'>Title:</h5>", unsafe_allow_html=True)

#st.write(personalised_graphics.map(accesos_prov_por_tecnologia, "ADSL", '#453824', '#F5B64F'))



"""container = st.container()
col1, col2, col3, col4 = container.columns(4)
with col1:
    
with col2:
    personalised_graphics.map(accesos_prov_por_tecnologia, "Cablemodem", '#1E311B', '#809F39')
with col3:
    personalised_graphics.map(accesos_prov_por_tecnologia, "Fibra óptica", '#051B32', '#015FA9')
with col4:
    personalised_graphics.map(accesos_prov_por_tecnologia, "Wireless", '#002D64', '#0F9EEA')"""