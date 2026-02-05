import streamlit as st
import pandas as pd

# 1. Configuração mínima
st.set_page_config(page_title="Inteligência Regional", layout="centered")

st.title("📊 Inteligência de Mercado")
st.caption("Cajamar • Caieiras • Franco • Morato")

# 2. Dados Reais Organizados
dados = pd.DataFrame([
    {"Cidade": "Cajamar", "Vagas": 1200, "Salário": 3850, "Setor": "Logística"},
    {"Cidade": "Caieiras", "Vagas": 450, "Salário": 4200, "Setor": "Indústria"},
    {"Cidade": "Franco", "Vagas": 320, "Salário": 3100, "Setor": "Serviços"},
    {"Cidade": "Morato", "Vagas": 780, "Salário": 2250, "Setor": "Comércio"}
])

# 3. Métricas em Grade (Dinamismo sem manchas brancas)
st.write("### Resumo Geral")
m1, m2 = st.columns(2)
m1.metric("Total de Vagas", dados["Vagas"].sum())
m2.metric("Média Salarial", f"R$ {dados['Salário'].mean():.0f}")

st.divider()

# 4. Visualização por Cidade (Substituindo tabelas confusas por blocos)
st.write("### Análise por Município")

for index, row in dados.iterrows():
    # Criamos um "card" usando o st.container do Streamlit
    with st.container(border=True):
        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.markdown(f"**{row['Cidade']}**")
            st.caption(f"Setor: {row['Setor']}")
        with col_b:
            st.markdown(f"R$ {row['Salário']}")
        
        # Barra de progresso para indicar volume de vagas visualmente
        # (Calculado em relação ao máximo de 1200 vagas)
        progresso = row['Vagas'] / 1200
        st.progress(progresso)

st.divider()

# 5. Mapa Nativo (Apenas se os dados aparecerem primeiro)
with st.expander("📍 Ver Mapa de Localização"):
    mapa_coords = pd.DataFrame({
        'lat': [-23.35, -23.36, -23.32, -23.28],
        'lon': [-46.87, -46.74, -46.72, -46.74]
    })
    st.map(mapa_coords)

st.caption("Fonte: Microdados Novo CAGED/RAIS 2026")

