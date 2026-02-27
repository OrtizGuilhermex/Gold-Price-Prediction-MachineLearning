import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('gold_prices_10y.csv')

df = df.dropna()

# 3. Selecionar Features (características) e Target (alvo)
# Vamos usar indicadores temporais e as médias móveis para prever o Close
features = ['Open', 'High', 'Low', 'Volume', 'MA_20', 'Volatility_20', 'Year', 'Month']
X = df[features]
y = df['Close']


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'modelo_ouro.pkl')
print("Modelo de Ouro treinado com sucesso!")