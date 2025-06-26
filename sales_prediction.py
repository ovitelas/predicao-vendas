import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import requests

# Download base de dados
url = 'https://www.statlearning.com/s/Advertising.csv'
response = requests.get(url)
with open('Advertising.csv', 'wb') as f:
    f.write(response.content)

# Carrega a base de dados
df = pd.read_csv('Advertising.csv', index_col=0)

# Divide os dados em recursos (X) e alvo (y)
X = df[['TV']]
y = df['sales']

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Realiza previsões no conjunto de teste
y_pred = model.predict(X_test)

# Calcula o erro quadrático médio (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'Root Mean Squared Error: {rmse}')

# Visualiza os resultados
plt.scatter(X, y, color='blue', label='Actual Sales')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Predicted Sales')
plt.title('Sales Prediction')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.legend()
plt.show()