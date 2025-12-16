import streamlit as st
import pandas as pd

from simulador import run_simulation

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
st.set_page_config(
    page_title="Simulador de Mercado Uber",
    layout="wide"
)

st.title("Simulador de Mercado Tipo Uber")
st.caption("Oferta, demanda y pricing dinámico")

# -----------------------------
# SIDEBAR – PARÁMETROS
# -----------------------------
st.sidebar.header("Parámetros del escenario")

steps = st.sidebar.slider(
    "Horizonte de simulación (ticks)",
    min_value=10,
    max_value=500,
    value=100
)

drivers = st.sidebar.slider(
    "Número de conductores",
    min_value=10,
    max_value=1000,
    value=200
)

users = st.sidebar.slider(
    "Número de usuarios",
    min_value=10,
    max_value=2000,
    value=500
)

base_price = st.sidebar.number_input(
    "Precio base",
    min_value=10.0,
    max_value=200.0,
    value=50.0
)

price_sensitivity = st.sidebar.slider(
    "Sensibilidad precio (surge)",
    min_value=0.0,
    max_value=0.05,
    value=0.01
)

# -----------------------------
# EJECUCIÓN
# -----------------------------
if st.sidebar.button("Ejecutar simulación"):

    params = {
        "steps": steps,
        "driver
