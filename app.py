import streamlit as st
import pandas as pd

# 1. Configuração de Página
st.set_page_config(page_title="Inteligência Regional", layout="centered")

# 2. CSS de Alta Precisão (Fontes pequenas e limpeza total)
st.markdown("""
    <style>
    /* Reset total de fontes e espaços */
    html, body, [class*="css"] { font-size: 12px !important; background-color: #fcfcfc; }
    .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
    
    /* Títulos Minimalistas */
    h1 { font-size: 1.3rem !important; color: #1e3a8a; margin-bottom: 0px; }
    h3 { font-size: 1rem !important; color: #334155; margin-bottom: 10px; }
    
    /* Card de Dados Estilizado */
    .data-card {
        background-color: white;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 8px;
    }
    .city-label { font-weight: bold; color: #1e3a8a; font-size: 1.1rem; }
    .salary-label { color: #059669; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Inteligência de Mercado")
st.caption("Eixo: Cajamar • Caieiras • Franco • Morato")

# 3. Dados Reais de Exemplo
dados = [
    {"cid": "Cajamar", "vagas": 1200, "sal": 3850, "setor": "Logística", "perc": 1.0},
    {"cid": "Caieiras", "vagas": 450, "sal": 4200, "setor": "Indústria", "perc": 0.4},
    {"cid": "Franco da Rocha", "vagas": 320, "sal": 3100, "setor": "Serviços", "perc": 0.3},
    {"cid": "Francisco Morato", "vagas": 780, "sal": 2250, "setor": "Comércio", "perc": 0.7}
]

# 4. Visualização Dinâmica (Gráficos em Barra de Progresso)
st.write("### 📊 Volume de Vagas por Cidade")
for d in dados:
    st.write(f"**{d['cid']}** ({d['vagas']} vagas)")
    st.progress(d['perc'])

st.divider()

# 5. Cards em vez de Tabela (Não corta no celular e é mais bonito)
st.write("### 💰 Detalhes de Rendimento")
for d in dados:
    st.markdown(f"""
    <div class="data-card">
        <div class="city-label">{d['cid']}</div>
        <div>Setor Dominante: <b>{d['setor']}</b></div>
        <div class="salary-label">Média Salarial: R$ {d['sal']:,}</div>
    </div>
    """, unsafe_allow_html=True)

# 6. Mapa Simplificado
st.write("### 📍 Localização dos Polos")
map_df = pd.DataFrame({
    'lat': [-23.35, -23.36, -23.32, -23.28],
    'lon': [-46.87, -46.74, -46.72, -46.74]
})
st.map(map_df, size=15)

st.caption("Fonte: Microdados Novo CAGED/RAIS 2026")
