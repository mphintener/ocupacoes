import streamlit as st
import pandas as pd

# 1. Configuração e CSS para forçar fontes pequenas e design limpo
st.set_page_config(page_title="Inteligência Regional", layout="centered")

st.markdown("""
    <style>
    /* Reduz a fonte global e títulos */
    html, body, [class*="css"] { font-size: 13px !important; }
    h1 { font-size: 1.4rem !important; color: #1E3A8A; font-weight: bold; }
    h3 { font-size: 1.1rem !important; margin-top: 20px; }
    
    /* Ajusta o espaçamento das métricas */
    [data-testid="stMetric"] { background-color: #f8f9fa; padding: 10px; border-radius: 8px; }
    
    /* Remove bordas excessivas das tabelas */
    .stDataFrame { border: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Inteligência de Mercado")
st.caption("Foco: Bacia do Juquery (Dados RAIS/CAGED)")

# 2. Dados Simplificados
data = {
    'Cidade': ['Cajamar', 'Caieiras', 'Franco da Rocha', 'Francisco Morato'],
    'Setor Principal': ['Logística', 'Indústria', 'TI/Serviços', 'Comércio'],
    'Vagas': [1200, 450, 320, 780],
    'Média Salarial': [3850.00, 4200.00, 3100.00, 2250.00],
    'lat': [-23.35, -23.36, -23.32, -23.28],
    'lon': [-46.87, -46.74, -46.72, -46.74]
}
df = pd.DataFrame(data)

# 3. Métricas Compactas
col1, col2 = st.columns(2)
with col1:
    st.metric("Total de Vagas", f"{df['Vagas'].sum()}")
with col2:
    st.metric("Maior Salário", f"R$ {df['Média Salarial'].max():.0f}")

# 4. Mapa Nativo (Muito mais limpo visualmente)
st.write("### 📍 Concentração Industrial")
# O st.map gera um mapa cinza/azul elegante automaticamente
st.map(df, size=20, color='#1E3A8A')

# 5. Tabela Organizada (Apenas as informações essenciais)
st.write("### 📊 Detalhes por Município")
# Usando o dataframe formatado para evitar confusão visual
st.dataframe(
    df[['Cidade', 'Setor Principal', 'Média Salarial']], 
    use_container_width=True,
    hide_index=True
)

st.divider()
st.caption("Fonte: Microdados do Novo CAGED - 2026")
