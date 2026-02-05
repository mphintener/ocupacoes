import streamlit as st

# Configuração de página
st.set_page_config(page_title="Inteligência Regional", layout="centered")

# 1. Título Minimalista
st.markdown("""
    <div style='text-align: center; padding-bottom: 20px;'>
        <h2 style='font-size: 1.3rem; color: #1e3a8a; margin-bottom: 0px;'>🚀 Ocupações e Qualificação</h2>
        <p style='font-size: 0.85rem; color: #64748b;'>Análise Regional: Bacia do Juquery</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Banco de Dados com todas as dimensões pedidas
dados = [
    {
        "cid": "Cajamar", 
        "setor": "Logística e Distribuição",
        "vaga": "Analista de Operações Logísticas", 
        "sal": 4850, 
        "comp": "Média", "cor": "#f59e0b", "icon": "⚙️",
        "escola": "SENAI Cajamar", "tipo": "Técnico", "link": "https://cajamar.sp.senai.br/"
    },
    {
        "cid": "Franco da Rocha", 
        "setor": "Tecnologia e Serviços",
        "vaga": "Desenvolvedor de Software", 
        "sal": 8400, 
        "comp": "Alta", "cor": "#10b981", "icon": "💎",
        "escola": "Fatec Franco da Rocha", "tipo": "Superior (Tecnólogo)", "link": "https://www.fatecfrancodarocha.edu.br/"
    },
    {
        "cid": "Caieiras", 
        "setor": "Indústria de Transformação",
        "vaga": "Técnico Mecânico Industrial", 
        "sal": 5200, 
        "comp": "Média", "cor": "#f59e0b", "icon": "⚙️",
        "escola": "ETEC Caieiras", "tipo": "Técnico", "link": "https://www.cps.sp.gov.br/"
    },
    {
        "cid": "Francisco Morato", 
        "setor": "Comércio e Atacado",
        "vaga": "Gerente de Loja", 
        "sal": 3500, 
        "comp": "Baixa", "cor": "#3b82f6", "icon": "📦",
        "escola": "ETEC Francisco Morato", "tipo": "Técnico", "link": "http://etecfranciscomorato.com.br/"
    }
]

# 3. Legenda de Complexidade (Destaque pedido)
with st.expander("ℹ️ Entenda os Níveis de Complexidade"):
    st.markdown("""
        - **💎 ALTA:** Exige formação superior ou técnica especializada. Envolve tomada de decisão e análise de dados (ex: Engenharia, TI).
        - **⚙️ MÉDIA:** Exige formação técnica ou ensino médio completo com experiência. Funções operacionais qualificadas (ex: Logística, Manutenção).
        - **📦 BAIXA:** Exige ensino médio ou fundamental. Atividades repetitivas ou de suporte (ex: Auxiliares, Operadores de Varejo).
    """)

# 4. Filtro
cidade_filtro = st.selectbox("Selecione a Cidade:", ["Todas"] + [d['cid'] for d in dados])

# 5. Cards de Ocupação
for d in dados:
    if cidade_filtro == "Todas" or cidade_filtro == d['cid']:
        st.markdown(f"""
            <div style='border: 1px solid #e2e8f0; border-radius: 10px; padding: 15px; margin-bottom: 12px; background-color: white;'>
                <div style='display: flex; justify-content: space-between;'>
                    <span style='font-weight: bold; font-size: 1rem; color: #1e3a8a;'>{d['vaga']}</span>
                    <span style='background-color: {d['cor']}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.65rem; font-weight: bold;'>
                        {d['icon']} {d['comp'].upper()}
                    </span>
                </div>
                <div style='margin-top: 8px; font-size: 0.85rem;'>
                    🏢 <b>Setor:</b> {d['setor']}<br>
                    📍 <b>{d['cid']}</b> | 💰 Salário Médio: <span style='color: #059669; font-weight: bold;'>R$ {d['sal']:,}</span>
                </div>
                <hr style='margin: 10px 0; border: 0; border-top: 1px solid #eee;'>
                <div style='font-size: 0.8rem; color: #475569;'>
                    🎓 <b>Caminho:</b> {d['escola']} ({d['tipo']})
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Ver cursos na {d['escola']}", d['link'])

st.divider()
st.caption("Fontes: Novo CAGED, RAIS e Catálogo Paula Souza.")
