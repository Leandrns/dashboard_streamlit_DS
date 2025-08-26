import streamlit as st

# --- Configuração da Página ---
# Use st.set_page_config() no início do seu script principal (app.py)
# st.set_page_config(page_title="Seu Nome | Portfólio", page_icon="👨‍💻", layout="wide")


# --- CAMINHOS DIRETOS PARA OS ARQUIVOS ---
# Coloque sua foto e CV em uma pasta chamada 'assets' no mesmo nível do seu script
resume_file = "assets/CURRICULO.pdf"
profile_pic = "assets/profile-pic.png"


# --- DADOS GERAIS ---
NAME = "Leandro do Nascimento Souza"
DESCRIPTION = """
Estagiário de QA, estudante de Engenharia de Software, com sonho de me tornar Desenvolvedor Full-Stack.
"""
EMAIL = "leandro2005souza@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/",
    "GitHub": "https://github.com/Leandrns",
}


# --- TÍTULO E CABEÇALHO ---
st.title("👨‍💻 Sobre Mim")
st.write("---")

# --- Layout com Colunas ---
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # --- Foto de Perfil ---
    try:
        st.image(profile_pic, width=230)
    except Exception as e:
        st.warning("Adicione uma foto de perfil em 'assets/profile-pic.png'")

    # --- Links Sociais e Contato ---
    st.write(f"📧 {EMAIL}")
    
    # Adiciona links
    st.write(" ".join([f"[{platform}]({link})" for platform, link in SOCIAL_MEDIA.items()]))
    
    # --- Botão de Download do Currículo ---
    try:
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Baixar Currículo",
            data=PDFbyte,
            file_name="CURRICULO.pdf", # Nome que o arquivo terá ao ser baixado
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.warning("Adicione seu currículo em 'assets/CURRICULO.pdf'")


with col2:
    st.header(NAME)
    st.write(DESCRIPTION)
    
    # --- Seção de Skills ---
    st.write("---")
    st.subheader("Hard Skills")
    st.write("""
    - 👩‍💻 **Linguagens:** Python, SQL, JavaScript, HTML/CSS
    - 📊 **Data Science & Vis:** Pandas, NumPy, Scikit-Learn, Plotly, Matplotlib
    - 🌐 **Front-End & Frameworks:** Streamlit, React, Node.js
    - 🗄️ **Bancos de Dados:** MySQL, PostgreSQL, MongoDB
    - ☁️ **Cloud & Ferramentas:** Git, Docker, AWS (S3, EC2)
    """)

    # --- Seção de Experiências ---
    st.write("---")
    st.subheader("Experiências Profissionais")

    # --- Experiência 1 ---
    with st.expander("🏢 Desenvolvedor de Dados | Empresa X (2022 - Presente)"):
        st.write("""
        - ► Desenvolvi e mantive pipelines de dados para processamento de grandes volumes de informação.
        - ► Criei dashboards interativos em Streamlit e Power BI para monitoramento de KPIs de negócio.
        - ► Apliquei modelos de machine learning para previsão de vendas, resultando em um aumento de 15% na precisão.
        """)
    
    # --- Seção de Formação Acadêmica ---
    st.write("---")
    st.subheader("Formação Acadêmica")

    # --- Formação 1 ---
    with st.expander("🎓 Bacharelado em Ciência da Computação | Universidade Z (2018 - 2022)"):
        st.write("""
        - ► TCC sobre a aplicação de algoritmos de processamento de linguagem natural para análise de sentimentos.
        - ► Participação em projetos de pesquisa na área de inteligência artificial.
        """)

    # --- Seção de Projetos ---
    st.write("---")
    st.subheader("Projetos em Destaque")
    st.write("[🔗 Dashboard de Análise de Vendas](link-para-o-projeto) - Um dashboard interativo construído com Streamlit para analisar dados de vendas de e-commerce.")
