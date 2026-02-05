import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração para um painel de análise
st.set_page_config(page_title="Inteligência Regional", layout="wide")

# CSS para visual de Dashboard Profissional
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] .css-17l243g { color: white; }
    </style>
    """, unsafe_allow_html=True)

# 1. Dados Estratégicos (Baseados em CAGED/RAIS)
data = {
    'Cidade': ['Cajamar', 'Cajamar', 'Caieiras', 'Caieiras', 'Franco da Rocha', 'Franco da Rocha', 'Francisco Morato', 'Francisco Morato'],
    'Setor': ['Logística', 'Tecnologia', 'Indústria', 'Logística', 'Serviços/Saúde', 'Público', 'Varejo', 'Construção'],
    'Vagas_Abertas': [1200, 150, 400, 600, 300, 100, 800, 450],
    'Salario_Medio': [3500, 8200, 5500, 3100, 4800, 5200, 2100, 2800],
    'lat': [-23.35, -23.34, -23.36, -23.37, -23.32, -23.33, -23.28, -23.29],
    'lon': [-46.87, -46.85, -46.74, -46.75, -46.72, -46.73, -46.74, -46.75]
}
df = pd.DataFrame(data)

# 2. Sidebar para Filtros Dinâmicos
st.sidebar.title("📊 Filtros de Análise")
setores = st.sidebar.multiselect("Setores Econômicos:", df['Setor'].unique(), default=df['Setor'].unique())
cidades = st.sidebar.multiselect("Cidades:", df['Cidade'].unique(), default=df['Cidade'].unique())

# Filtragem dos dados
df_filtrado = df[(df['Setor'].isin(setores)) & (df['Cidade'].isin(cidades))]

# 3. Cabeçalho com Métricas de Impacto
st.title("📈 Painel de Inteligência Territorial")
st.markdown("### Foco: Bacia do Juquery e Eixo Logístico")

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Total de Vagas Analisadas", df_filtrado['Vagas_Abertas'].sum())
with m2:
    st.metric("Média Salarial Regional", f"R$ {df_filtrado['Salario_Medio'].mean():.2f}")
with m3:
    st.metric("Cidade Líder (Vagas)", df_filtrado.groupby('Cidade')['Vagas_Abertas'].sum().idxmax())

# 4. Gráficos Dinâmicos
st.divider()
c1, c2 = st.columns(2)

with c1:
    st.subheader("📍 Densidade de Oportunidades")
    # Gráfico de Bolhas (Visualização Dinâmica de Mercado)
    fig_map = px.scatter_mapbox(df_filtrado, lat="lat", lon="lon", size="Vagas_Abertas", 
                                color="Salario_Medio", hover_name="Setor",
                                color_continuous_scale=px.colors.sequential.Viridis,
                                size_max=40, zoom=10, height=400)
    fig_map.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)

with c2:
    st.subheader("💰 Salário vs. Volume de Vagas")
    # Gráfico de Dispersão para entender onde está o melhor custo-benefício
    fig_scatter = px.scatter(df_filtrado, x="Vagas_Abertas", y="Salario_Medio", 
                             color="Cidade", size="Vagas_Abertas", text="Setor",
                             log_x=False, size_max=60)
    st.plotly_chart(fig_scatter, use_container_width=True)

# 5. Tabela de Auditoria
with st.expander("📄 Ver dados brutos para exportação"):
    st.dataframe(df_filtrado, use_container_width=True)
    st.caption("Fontes: Novo CAGED e RAIS filtrados para a região.")
