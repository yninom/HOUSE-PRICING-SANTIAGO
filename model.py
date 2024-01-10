import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Load the dataset
data = pd.read_csv("Casas.csv")

# Split the data into features (X) and target variable (y)
X = data.drop("Precio", axis=1)
y = data["Precio"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the prices for the test data
y_pred = model.predict(X_test)
def predict_price(habitaciones, piso, barrio):
    # Create a dataframe with the input values
    input_data = pd.DataFrame({'Habitaciones': [habitaciones], 'Piso': [piso], 'Barrio': [barrio]})
    
    # Use the trained model to predict the price
    predicted_price = model.predict(input_data)
    
    return predicted_price[0]

