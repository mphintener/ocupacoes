import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Regional Ocupações", layout="centered")

# CSS para garantir que o texto apareça
st.markdown("<style>h1, h3 { color: #1E3A8A; } .stExpander { background-color: white; }</style>", unsafe_allow_html=True)

st.title("📍 Inteligência Regional")

# 1. DADOS DE ENSINO (Garantindo que apareçam)
instituicoes = [
    {"nome": "Fatec Franco da Rocha", "cid": "Franco da Rocha", "link": "https://www.fatecfrancodarocha.edu.br/"},
    {"nome": "ETEC Francisco Morato", "cid": "Francisco Morato", "link": "https://www.cps.sp.gov.br/"},
    {"nome": "Anhanguera Caieiras", "cid": "Caieiras", "link": "https://www.anhanguera.com/"},
    {"nome": "Senai Cajamar", "cid": "Cajamar", "link": "https://cajamar.sp.senai.br/"}
]

# 2. DADOS DE OCUPAÇÕES
ocupacoes = [
    {"cargo": "Desenvolvedor", "cid": "Cajamar", "sal": "R$ 8.500", "comp": "Alta"},
    {"cargo": "Logística", "cid": "Cajamar", "sal": "R$ 4.200", "comp": "Média"},
    {"cargo": "Indústria", "cid": "Caieiras", "sal": "R$ 6.800", "comp": "Alta"},
    {"cargo": "Varejo", "cid": "Morato", "sal": "R$ 2.150", "comp": "Baixa"}
]

# --- NAVEGAÇÃO ---
aba1, aba2 = st.tabs(["🔍 Ocupações e Ensino", "🔥 Mapa de Calor"])

with aba1:
    st.subheader("Onde Trabalhar e Estudar")
    # Filtro simples
    filtro_cidade = st.selectbox("Escolha a Cidade", ["Todas", "Cajamar", "Caieiras", "Franco da Rocha", "Francisco Morato"])
    
    st.write("### 💼 Ocupações")
    for o in ocupacoes:
        if filtro_cidade == "Todas" or o['cid'] == filtro_cidade:
            with st.expander(f"{o['cargo']} - {o['cid']}"):
                st.write(f"**Salário:** {o['sal']} | **Nível:** {o['comp']}")

    st.write("### 🏫 Instituições")
    for i in instituicoes:
        if filtro_cidade == "Todas" or i['cid'] == filtro_cidade:
            st.markdown(f"**{i['nome']}** ({i['cid']})")
            st.link_button("Ver Cursos", i['link'])

with aba2:
    st.subheader("🔥 Mancha de Renda")
    # Dados para o mapa (Lat/Lon reais da região)
    mapa_df = pd.DataFrame({
        'lat': [-23.33, -23.36, -23.35, -23.28],
        'lon': [-46.72, -46.74, -46.87, -46.74],
        'peso': [80, 60, 90, 30] # Intensidade do calor
    })
    
    layer = pdk.Layer(
        "HeatmapLayer",
        mapa_df,
        get_position='[lon, lat]',
        get_weight='peso',
        radius_pixels=50
    )
    
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=pdk.ViewState(latitude=-23.34, longitude=-46.76, zoom=10)
    ))

st.caption("v3.0 - Dados Regionais Atualizados")
