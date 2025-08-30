import streamlit as st
import pandas as pd
import plotly.express as px


# Configurações da página
st.set_page_config(
    page_title="Dashboard de Vendas - Supermercado",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar CSS externo
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Estilo de gráfico padrão
px.defaults.template = "plotly_white"
px.defaults.color_continuous_scale = "Aggrnyl"

# Título principal
st.markdown(
    """
    <div class="titulo-principal">📈 Dashboard de Vendas - Supermercado</div>
    """,
    unsafe_allow_html=True
)

# Importar dados
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",", encoding="utf-8")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month).zfill(2))

# Filtros na barra lateral
st.sidebar.header("🔍 Filtros")
mes = st.sidebar.selectbox("Selecione o mês:", df["Month"].unique())
df_filtrado = df[df["Month"] == mes]

# KPIs principais
st.markdown("### 🔢 Visão Geral do Mês Selecionado")
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

total_vendas = df_filtrado["Total"].sum()
media_avaliacao = df_filtrado["Rating"].mean()
cidade_top = df_filtrado.groupby("City")["Total"].sum().idxmax()

col_kpi1.metric("💰 Total de Vendas", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col_kpi2.metric("⭐ Média de Avaliação", f"{media_avaliacao:.2f}")
col_kpi3.metric("🏙️ Cidade com Maior Faturamento", cidade_top)

# Seção de faturamento por data e produto
st.markdown("### 📅 Faturamento por Data")
col1, col2 = st.columns([2, 1])

fig_data = px.bar(
    df_filtrado,
    x="Date",
    y="Total",
    color="City",
    title="Vendas ao Longo do Mês",
    labels={"Total": "Faturamento", "Date": "Data"},
)
col1.plotly_chart(fig_data, use_container_width=True)

# Produto mais vendido
df_produto = df_filtrado.groupby("Product line")["Total"].sum().reset_index().sort_values("Total", ascending=True)
fig_produto = px.bar(
    df_produto,
    x="Total",
    y="Product line",
    orientation="h",
    title="Top Produtos por Faturamento",
    color="Total",
    color_continuous_scale="Viridis",
    labels={"Total": "Faturamento", "Product line": "Linha de Produto"}
)
col2.plotly_chart(fig_produto, use_container_width=True)

# Seção de análise por cidade e forma de pagamento
st.markdown("### 🏪 Análises por Filial e Pagamento")
col3, col4, col5 = st.columns(3)

# Faturamento por cidade
df_cidade = df_filtrado.groupby("City")["Total"].sum().reset_index()
fig_cidade = px.bar(
    df_cidade,
    x="City",
    y="Total",
    color="City",
    title="Faturamento por Filial",
    labels={"Total": "Faturamento", "City": "Cidade"}
)
col3.plotly_chart(fig_cidade, use_container_width=True)

# Faturamento por forma de pagamento
fig_pagamento = px.pie(
    df_filtrado,
    values="Total",
    names="Payment",
    title="Distribuição por Forma de Pagamento",
    hole=0.4
)
col4.plotly_chart(fig_pagamento, use_container_width=True)

# Avaliação média por cidade
df_avaliacao = df_filtrado.groupby("City")["Rating"].mean().reset_index()
fig_avaliacao = px.bar(
    df_avaliacao,
    x="City",
    y="Rating",
    color="City",
    title="Avaliação Média por Cidade",
    labels={"Rating": "Nota Média", "City": "Cidade"}
)
col5.plotly_chart(fig_avaliacao, use_container_width=True)

# Contribuição percentual por cidade
st.markdown("### 📊 Participação de Faturamento por Cidade")
df_contrib = df_filtrado.groupby("City")["Total"].sum().reset_index()
df_contrib["% do Total"] = 100 * df_contrib["Total"] / df_contrib["Total"].sum()

fig_contrib = px.pie(
    df_contrib,
    names="City",
    values="% do Total",
    title="Contribuição % no Faturamento",
    hole=0.5
)
st.plotly_chart(fig_contrib, use_container_width=True)

# Rodapé
st.markdown(
    """
    <hr style="margin-top: 30px; margin-bottom: 10px;">
    <div style="text-align: center; color: #888888;">
        Desenvolvido por Vitor Barbosa · Projeto com Streamlit + Plotly Express · 2025
    </div>
    """,
    unsafe_allow_html=True
)