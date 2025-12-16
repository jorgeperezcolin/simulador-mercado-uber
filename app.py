import streamlit as st
import pandas as pd

# IMPORTA TU SIMULADOR
# ajusta el import según el nombre real del archivo
from simulador import run_simulation  

st.set_page_config(
    page_title="Simulador de Mercado Uber",
    layout="wide"
)

st.title("Simulador de Mercado Tipo Uber")
st.caption("Simulación de interacción oferta–demanda con pricing dinámico")

# -----------------------------
# CONTROLES
# -----------------------------
st.sidebar.header("Parámetros del mercado")

num_steps = st.sidebar.slider(
    "Horizonte de simulación (ticks)",
    min_value=10,
    max_value=500,
    value=100
)

num_drivers = st.sidebar.slider(
    "Número de conductores",
    min_value=10,
    max_value=1000,
    value=200
)

num_users = st.sidebar.slider(
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

# -----------------------------
# EJECUCIÓN
# -----------------------------
if st.sidebar.button("Ejecutar simulación"):

    params = {
        "steps": num_steps,
        "drivers": num_drivers,
        "users": num_users,
        "base_price": base_price
    }

    st.subheader("Parámetros del escenario")
    st.json(params)

    # Ejecuta el modelo
    results = run_simulation(params)

    # Aseguramos DataFrame
    df = pd.DataFrame(results)

    # -----------------------------
    # OUTPUT EJECUTIVO
    # -----------------------------
    st.subheader("Resultados del mercado")

    col1, col2, col3 = st.columns(3)
    col1.metric("Precio promedio", round(df["price"].mean(), 2))
    col2.metric("Viajes totales", int(df["trips"].sum()))
    col3.metric("Utilización conductores", round(df["utilization"].mean(), 2))

    st.subheader("Evolución temporal")
    st.line_chart(
        df.set_index("step")[["price", "trips", "utilization"]]
    )

    st.subheader("Detalle por iteración")
    st.dataframe(df)
