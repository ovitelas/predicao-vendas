import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import requests

# Download the dataset
url = 'https://www.statlearning.com/s/Advertising.csv'
response = requests.get(url)
with open('Advertising.csv', 'wb') as f:
    f.write(response.content)

# Load the dataset
df = pd.read_csv('Advertising.csv', index_col=0)

# Split the data into features (X) and target (y)
# For this example, we'll use 'TV' as the feature
X = df[['TV']]
y = df['sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'Root Mean Squared Error: {rmse}')

# Visualize the results
plt.scatter(X, y, color='blue', label='Actual Sales')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Predicted Sales')
plt.title('Sales Prediction')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.legend()
plt.show()