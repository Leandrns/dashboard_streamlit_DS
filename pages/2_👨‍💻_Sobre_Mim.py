import streamlit as st

st.title("👨‍💻 Sobre Mim")

st.write("""
Olá! Eu sou **Seu Nome**, desenvolvedor com foco em **Data Science e Front-End**.  
Aqui estão algumas das minhas skills principais:
- Python (Pandas, Streamlit, Scikit-Learn)
- SQL
- React e desenvolvimento Front-End
- Visualização de dados

""")

st.download_button(
    label="📄 Baixar Currículo",
    data=open("CURRICULO.pdf", "rb").read(),
    file_name="CURRICULO.pdf",
    mime="application/pdf"
)
