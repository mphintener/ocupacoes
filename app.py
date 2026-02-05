import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Mudança para layout centered para evitar faixas brancas no mobile
st.set_page_config(page_title="Inteligência Regional", layout="centered")

# 2. CSS Corretivo para Mobile
st.markdown("""
    <style>
    /* Remove espaços vazios no topo e evita sobreposição */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    /* Força o gráfico a caber na tela sem criar barras brancas */
    .stPlotlyChart {
        width: 100% !important;
        overflow: hidden;
    }
    /* Estilização das métricas para não quebrarem */
    [data-testid="stMetricValue"] {
        font-size: 1.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Painel Estratégico")
st.caption("Bacia do Juquery • Inteligência de Dados")

# Dados (Mantive os mesmos para teste)
data = {
    'Cidade': ['Cajamar', 'Caieiras', 'Franco', 'Morato'],
    'Vagas': [1200, 400, 300, 800],
    'Salario': [3500, 5500, 4800, 2100],
    'lat': [-23.35, -23.36, -23.32, -23.28],
    'lon': [-46.87, -46.74, -46.72, -46.74]
}
df = pd.DataFrame(data)

# 3. Métricas empilhadas (Melhor para celular que colunas lado a lado)
st.metric("Total de Vagas", df['Vagas'].sum())
st.metric("Média Salarial", f"R$ {df['Salario'].mean():.2f}")

st.divider()

# 4. Gráfico de Mapa (Simplificado para evitar erro visual)
st.subheader("📍 Mapa de Oportunidades")
fig_map = px.scatter_mapbox(df, lat="lat", lon="lon", size="Vagas", 
                            color="Salario", hover_name="Cidade",
                            color_continuous_scale=px.colors.sequential.Bluered,
                            size_max=30, zoom=9, height=350)

fig_map.update_layout(
    mapbox_style="carto-positron", 
    margin={"r":0,"t":0,"l":0,"b":0},
    autosize=True
)
st.plotly_chart(fig_map, use_container_width=True)

# 5. Gráfico de Barras Vertical (Melhor que o de dispersão no mobile)
st.subheader("💰 Salário por Cidade")
fig_bar = px.bar(df, x='Cidade', y='Salario', color='Cidade', height=300)
fig_bar.update_layout(showlegend=False, margin={"r":10,"t":10,"l":10,"b":10})
st.plotly_chart(fig_bar, use_container_width=True)

with st.expander("📄 Ver dados da RAIS/CAGED"):
    st.dataframe(df, use_container_width=True)
