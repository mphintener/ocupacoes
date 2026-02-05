import streamlit as st

# Configuração de página
st.set_page_config(page_title="Inteligência Regional Juquery", layout="centered")

# 1. Título e Subtítulo Minimalistas
st.markdown("""
    <div style='text-align: center; padding-bottom: 20px;'>
        <h2 style='font-size: 1.3rem; color: #1e3a8a; margin-bottom: 0px;'>🚀 Ocupações e Qualificação</h2>
        <p style='font-size: 0.85rem; color: #64748b;'>Cajamar • Caieiras • Franco • Morato</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Banco de Dados Integrado (Vagas + Setor + Ensino)
dados = [
    {
        "cid": "Cajamar", 
        "setor": "Logística e Transportes",
        "vaga": "Analista de Operações Logísticas", 
        "sal": 4500, 
        "comp": "Média", "cor": "#f59e0b", "icon": "⚙️",
        "escola": "SENAI Cajamar", "tipo": "Técnico", "link": "https://cajamar.sp.senai.br/"
    },
    {
        "cid": "Franco da Rocha", 
        "setor": "Tecnologia da Informação",
        "vaga": "Desenvolvedor de Software Full Stack", 
        "sal": 8200, 
        "comp": "Alta", "cor": "#10b981", "icon": "💎",
        "escola": "Fatec Franco da Rocha", "tipo": "Superior (Tecnólogo)", "link": "https://www.fatecfrancodarocha.edu.br/"
    },
    {
        "cid": "Caieiras", 
        "setor": "Indústria e Manufatura",
        "vaga": "Técnico de Manutenção Industrial", 
        "sal": 5100, 
        "comp": "Média", "cor": "#f59e0b", "icon": "⚙️",
        "escola": "ETEC Caieiras", "tipo": "Técnico", "link": "https://www.cps.sp.gov.br/"
    },
    {
        "cid": "Francisco Morato", 
        "setor": "Comércio e Serviços",
        "vaga": "Gerente de Loja e Varejo", 
        "sal": 3100, 
        "comp": "Baixa", "cor": "#3b82f6", "icon": "📦",
        "escola": "ETEC Francisco Morato", "tipo": "Técnico", "link": "http://etecfranciscomorato.com.br/"
    }
]

# 3. Filtro de Cidade
cidade_filtro = st.selectbox("Filtrar por Município:", ["Todas as Cidades"] + sorted(list(set(d['cid'] for d in dados))))

# 4. Exibição Dinâmica
st.write("### Oportunidades por Setor e Formação")

for d in dados:
    if cidade_filtro == "Todas as Cidades" or cidade_filtro == d['cid']:
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
                    📍 <b>{d['cid']}</b> | 💰 Média: <b>R$ {d['sal']:,}</b>
                </div>
                <hr style='margin: 10px 0; border: 0; border-top: 1px solid #eee;'>
                <div style='font-size: 0.8rem; color: #475569;'>
                    🎓 <b>Formação:</b> {d['escola']} ({d['tipo']})
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.link_button(f"Explorar Cursos na {d['escola']}", d['link'])

# 5. Nota de Rodapé
st.divider()
st.caption("Fontes: Estrutura Setorial RAIS/CAGED e Catálogo de Cursos Técnicos/Superiores.")

