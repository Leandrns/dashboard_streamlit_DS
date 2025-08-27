import streamlit as st

# --- Configuração da Página ---
# Use st.set_page_config() no início do seu script principal (app.py)
st.set_page_config(page_title="Leandro Souza | Sobre Mim", layout="wide")

st.sidebar.markdown("<p style='text-align: center; font-size: 12px'>Desenvolvido por <strong>Leandro Souza<strong></p>", unsafe_allow_html=True)

# --- CAMINHOS DIRETOS PARA OS ARQUIVOS ---
# Coloque sua foto e CV em uma pasta chamada 'assets' no mesmo nível do seu script
resume_file = "assets/CURRICULO.pdf"
profile_pic = "assets/foto_perfil.jpeg"


# --- DADOS GERAIS ---
NAME = "Leandro do Nascimento Souza"
DESCRIPTION = """
Estagiário de QA, estudante de Engenharia de Software, com sonho de me tornar Desenvolvedor Full-Stack.
"""
EMAIL = "leandro2005souza@gmail.com"

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

    coluna1, coluna2 = st.columns([1, 8], gap="small")
    
    # Adiciona links
    with coluna1:
        st.image("./assets/github-brands-solid-full.svg", width=36)
        st.image("./assets/linkedin-brands-solid-full.svg", width=36)
    with coluna2:    
        st.write("[GitHub](https://github.com/Leandrns)")
        st.write("[LinkedIn](https://linkedin.com/in/leandro-souza-326722181)")
    
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
    st.subheader("Skills")
    st.write("""
    - 👩‍💻 **Linguagens:** Python, SQL, JavaScript, HTML/CSS, Java, C++
    - 📊 **Data Science:** Pandas, NumPy, Scipy, Plotly, Matplotlib
    - 🌐 **Front-End & Frameworks:** Streamlit, React, Sass, Node.js, Vite
    - 🗄️ **Bancos de Dados:** MySQL, PostgreSQL, Oracle
    - 🔨 **Ferramentas:** Git, Docker, Figma, Postman
    """)

    # --- Seção de Experiências ---
    st.write("---")
    st.subheader("Experiências Profissionais")

    # --- Experiência 1 ---
    with st.expander("🏢 Estágio em Qualidade (QA) | NeoAssist (2025 - Presente)"):
        st.write("""
        - Elaboração de testes de Bots e Centrais de Atendimento.
        - Participação em reuniões e rituais de SCRUM.
        """)
    
    # --- Seção de Formação Acadêmica ---
    st.write("---")
    st.subheader("Formação Acadêmica")

    # --- Formação 1 ---
    with st.expander("🎓 Ensino Médio Técnico em Mecatrônica | ETEC Presidente Vargas (2021 - 2023)"):
        st.write("""
        - TCC sobre uso da robótica em terapia assistiva para crianças com paralisia cerebral.
        - Participação em projetos de programação, mecânica e eletrônica.
        """)
        
    # --- Formação 2 ---
    with st.expander("🎓 Bacharelado em Engenharia de Software | FIAP (2024 - 2027)"):
        st.write("""
        - Desenvolvimento de projetos de Front-End, Back-End, Análise de Dados, Inteligência Artificial e outros.
        - Participação em Iniciação Científica sobre aplicação de Realidadde Aumentada para autoajuda.
        """)