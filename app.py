import streamlit as st
import pandas as pd

# Configuração simples
st.set_page_config(page_title="Regional Ocupações", page_icon="📍")

st.title("📍 Inteligência Regional")
st.markdown("Cajamar • Caieiras • Franco • Morato")

# --- DADOS ---
# Ocupações
df_ocup = pd.DataFrame([
    {"Cargo": "Analista de Logística", "Cidade": "Cajamar", "Salário": "R$ 4.200", "Nível": "Média"},
    {"Cargo": "Desenvolvedor", "Cidade": "Cajamar", "Salário": "R$ 8.500", "Nível": "Alta"},
    {"Cargo": "Técnico Industrial", "Cidade": "Caieiras", "Salário": "R$ 5.800", "Nível": "Alta"},
    {"Cargo": "Enfermeiro", "Cidade": "Franco da Rocha", "Salário": "R$ 6.500", "Nível": "Alta"},
    {"Cargo": "Comércio", "Cidade": "Francisco Morato", "Salário": "R$ 2.150", "Nível": "Baixa"}
])

# Instituições
df_inst = pd.DataFrame([
    {"Nome": "Fatec Franco da Rocha", "Cidade": "Franco da Rocha", "lat": -23.335, "lon": -46.722},
    {"Nome": "ETEC Francisco Morato", "Cidade": "Francisco Morato", "lat": -23.289, "lon": -46.746},
    {"Nome": "Anhanguera Caieiras", "Cidade": "Caieiras", "lat": -23.360, "lon": -46.744},
    {"Nome": "Senai Cajamar", "Cidade": "Cajamar", "lat": -23.355, "lon": -46.877}
])

# --- INTERFACE ---
aba1, aba2 = st.tabs(["🔍 Ocupações e Ensino", "📍 Localização"])

with aba1:
    st.subheader("Filtro por Município")
    escolha = st.selectbox("Selecione:", ["Todas"] + list(df_ocup['Cidade'].unique()))
    
    # Filtragem
    vagas = df_ocup if escolha == "Todas" else df_ocup[df_ocup['Cidade'] == escolha]
    ensino = df_inst if escolha == "Todas" else df_inst[df_inst['Cidade'] == escolha]

    st.write("### 💼 Ocupações Encontradas")
    for _, item in vagas.iterrows():
        st.info(f"**{item['Cargo']}**\n\n{item['Cidade']} | {item['Salário']} ({item['Nível']})")

    st.write("### 🏫 Onde Estudar")
    for _, inst in ensino.iterrows():
        st.success(f"**{inst['Nome']}**\n\nLocalizada em: {inst['Cidade']}")

with aba2:
    st.subheader("Mapa de Instituições")
    # O st.map é nativo e não causa erro de 'tela branca'
    st.map(df_inst[['lat', 'lon']])

st.caption("v3.1 - Estabilidade Total")
