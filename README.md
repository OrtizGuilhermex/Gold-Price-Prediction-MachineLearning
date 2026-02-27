# 💰 Gold Price Prediction - Machine Learning & Streamlit

Este repositório contém o desenvolvimento de uma aplicação de Machine Learning de ponta a ponta (End-to-End) para a previsão do preço do ouro, baseada em dados históricos de 10 anos. Este projeto faz parte da Atividade Prática da disciplina de **Data Science**.

---

## 🎯 Objetivo

O objetivo é aplicar modelos de regressão para prever o preço de fechamento (`Close`) do ouro com base em indicadores de mercado como preço de abertura, máxima, mínima, volume e médias móveis.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
|---|---|
| Linguagem | Python 3.9+ |
| Bibliotecas de ML | Scikit-Learn, Pandas, Numpy |
| Persistência de Modelo | Joblib |
| Interface Gráfica | Streamlit |
| Algoritmo | Random Forest Regressor |

---

## 📁 Estrutura do Projeto

```text
/gold-price-prediction/
├── train.py              # Script de tratamento de dados e treinamento do modelo
├── app.py                # Aplicação web interativa com Streamlit
├── modelo_ouro.pkl       # Modelo treinado salvo (binário)
├── requirements.txt      # Lista de dependências do projeto
└── gold_prices_10y.csv   # Dataset utilizado
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as dependências

Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual.

```bash
pip install -r requirements.txt
```

### 3. Treinar o modelo *(Opcional se o `.pkl` já existir)*

Para gerar ou atualizar o modelo treinado:

```bash
python train.py
```

### 4. Rodar a aplicação Streamlit

```bash
streamlit run app.py
```

---

## 📊 Funcionalidades

- **Interface Interativa:** O usuário pode inserir valores de `Open`, `High`, `Low` e `Volume` através de campos numéricos.
- **Previsão em Tempo Real:** Ao clicar no botão, o modelo processa os dados e exibe a estimativa do valor de fechamento.
- **Indicadores Técnicos:** O app permite simular cenários alterando a Volatilidade e Médias Móveis (`MA_20`).

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
