import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Inteligência Regional", layout="wide")

st.title("📊 Painel Estratégico: Bacia do Juquery")

# 1. Simulação de Dados Reais (Onde estão as vagas de alta renda)
# No futuro, este DataFrame será preenchido pelo seu CSV do CAGED
data_map = pd.DataFrame({
    'lat': [-23.33, -23.36, -23.35, -23.28, -23.32, -23.34],
    'lon': [-46.72, -46.74, -46.87, -46.74, -46.73, -46.85],
    'renda': [8000, 4500, 9000, 2500, 5000, 7000],
    'vagas': [10, 50, 5, 100, 20, 15]
})

# 2. Mapa de Calor (Heatmap)
st.subheader("🔥 Concentração de Renda e Ocupações")
st.write("Manchas de calor baseadas no volume de salários por região (Cajamar e Caieiras em destaque).")

layer = pdk.Layer(
    "HeatmapLayer",
    data_map,
    get_position='[lon, lat]',
    get_weight='renda',
    radius_pixels=60,
)

view_state = pdk.ViewState(latitude=-23.34, longitude=-46.76, zoom=10, pitch=0)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "Concentração de Renda"}
))



# 3. Comparativo entre Cidades (Dados que você minerou)
st.subheader("📈 Comparativo Socioeconômico")
col1, col2 = st.columns(2)

with col1:
    st.write("**Salário Médio por Cidade**")
    chart_data = pd.DataFrame({
        'Cidade': ['Cajamar', 'Caieiras', 'Franco', 'Morato'],
        'R$': [4200, 3800, 2900, 2100]
    }).set_index('Cidade')
    st.bar_chart(chart_data)

with col2:
    st.write("**Complexidade vs Qualificação**")
    st.info("Cajamar e Caieiras lideram em ocupações de 'Alta Complexidade' devido aos pólos logísticos e industriais.")

st.markdown("---")
st.button("Baixar Relatório Completo (CSV)")
