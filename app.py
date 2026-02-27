import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Preditor de Preço do Ouro", page_icon="💰")

model = joblib.load('modelo_ouro.pkl')

st.title("💰 Previsão de Valor do Ouro (ML)")
st.markdown("Insira os dados do mercado para prever o preço de fechamento.")

col1, col2 = st.columns(2)

with col1:
    open_val = st.number_input("Preço de Abertura (Open)", value=400.0)
    high_val = st.number_input("Máxima do Dia (High)", value=405.0)
    low_val = st.number_input("Mínima do Dia (Low)", value=395.0)
    vol = st.number_input("Volume Negociado", value=15000000)

with col2:
    ma20 = st.number_input("Média Móvel (MA_20)", value=400.0)
    volatility = st.number_input("Volatilidade (20 dias)", value=1.5)
    year = st.selectbox("Ano", [2024, 2025, 2026])
    month = st.slider("Mês", 1, 12, 1)


if st.button("Calcular Preço Estimado"):
    input_data = pd.DataFrame([[open_val, high_val, low_val, vol, ma20, volatility, year, month]], 
                              columns=['Open', 'High', 'Low', 'Volume', 'MA_20', 'Volatility_20', 'Year', 'Month'])
    
    predicao = model.predict(input_data)[0]
    
    st.divider()
    st.metric(label="Preço de Fechamento Estimado", value=f"US$ {predicao:.2f}")
    st.info("Nota: Este é um modelo educacional baseado em dados históricos.")