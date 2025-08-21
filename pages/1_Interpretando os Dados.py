import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Interpretando os Dados",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interpretando os Dados do Dataset")

st.write("### Dataset:")
st.markdown(
    "[Link para o dataset no Kaggle](https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction?resource=download)"
)

# -----------------------------
# Upload do arquivo CSV
# -----------------------------
st.write("### 📂 Carregar dataset")

uploaded_file = st.file_uploader("Faça upload do arquivo CSV do dataset", type=["csv"])

if uploaded_file is not None:
    df_data = pd.read_csv(uploaded_file)
    st.success("✅ Arquivo carregado com sucesso!")
    st.write("#### Prévia dos dados:")
    st.dataframe(df_data.head(), use_container_width=True)


st.write("### 📑 Colunas e tipos de dados")

# Criando a tabela com Pandas
data_dict = {
    "Nome da coluna": [
        "Unique_id", "channel_name", "category", "Sub-category",
        "Customer_Remarks", "Order_id", "order_date_time", "Issue_reported_at",
        "issue_responded", "Survey_response_Date", "Customer_City",
        "Product_category", "Item_price", "connected_handling_time",
        "Agent_name", "Supervisor", "Manager", "Tenure_Bucket",
        "Agent_Shift", "CSAT_Score"
    ],
    "Descrição": [
        "Identificador único para cada registro",
        "Nome do canal de atendimento ao cliente",
        "Categoria da interação",
        "Subcategoria da interação",
        "Feedback fornecido pelo cliente",
        "Identificador do pedido associado à interação",
        "Data e hora do pedido",
        "Carimbo de data e hora em que o problema foi relatado",
        "Carimbo de data e hora em que o problema foi respondido",
        "Data da resposta da pesquisa do cliente",
        "Cidade do cliente",
        "Categoria do produto",
        "Preço do item",
        "Tempo gasto para lidar com a interação (COLUNA SEM DADOS)",
        "Nome do agente de atendimento ao cliente",
        "Nome do supervisor",
        "Nome do gerente",
        "Agente de categorização de buckets (tempo de casa, em dias)",
        "Tempo de turno do agente",
        "Pontuação de satisfação do cliente (CSAT)"
    ],
    "Tipo de dado": [
        "Qualitativo Nominal", "Qualitativo Nominal", "Qualitativo Nominal",
        "Qualitativo Nominal", "Qualitativo Nominal", "Qualitativo Nominal",
        "Quantitativo Contínuo", "Quantitativo Contínuo", "Quantitativo Contínuo",
        "Quantitativo Discreto", "Qualitativo Nominal", "Qualitativo Nominal",
        "Quantitativo Contínuo", "Quantitativo Contínuo", "Qualitativo Nominal",
        "Qualitativo Nominal", "Qualitativo Nominal", "Qualitativo Ordinal",
        "Qualitativo Nominal", "Quantitativo Discreto"
    ]
}

df = pd.DataFrame(data_dict)

# Exibir como tabela interativa
st.dataframe(df, use_container_width=True)

