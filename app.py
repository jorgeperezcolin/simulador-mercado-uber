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
    "Sensibilidad del surge pricing",
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
        "drivers": drivers,
        "users": users,
        "base_price": base_price,
        "price_sensitivity": price_sensitivity
    }

    st.subheader("Parámetros del escenario")
    st.json(params)

    # Ejecutar simulación
    results = run_simulation(params)
    df = pd.DataFrame(results)

    # -----------------------------
    # KPIs EJECUTIVOS
    # -----------------------------
    st.subheader("KPIs del mercado")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Precio promedio",
        f"${df['price'].mean():.2f}"
    )

    col2.metric(
        "Viajes totales",
        int(df["trips"].sum())
    )

    col3.metric(
        "Utilización de conductores",
        f"{df['utilization'].mean():.2%}"
    )

    # -----------------------------
    # VISUALIZACIONES
    # -----------------------------
    st.subheader("Evolución temporal")

    st.line_chart(
        df.set_index("step")[["price", "trips", "utilization"]]
    )

    # -----------------------------
    # TABLA DETALLADA
    # -----------------------------
    st.subheader("Detalle por tick")
    st.dataframe(df)

    # -----------------------------
    # DESCARGA
    # -----------------------------
    csv = df.to_csv(index=False)
    st.download_button(
        "Descargar resultados (CSV)",
        csv,
        file_name="resultados_simulacion.csv",
        mime="text/csv"
    )
