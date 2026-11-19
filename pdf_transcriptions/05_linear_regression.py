# Question: Demonstrate Linear Regression and predict an output for a given input.
# Transcribed from the manual; indentation restored for Python readability.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

# Step 1: Load the dataset
data = pd.read_csv("/home/sahyadri/AIML Dataset/train.csv")
print("First 5 rows of the dataset:")
print(data.head())
print("\nDataset Shape:")
print(data.shape)

# Step 2: Perform basic EDA
print("\nColumn Names:")
print(data.columns)
print("\nMissing Values:")
print(data.isnull().sum().sort_values(ascending=False).head(10))

# Step 3: Find correlation with SalePrice
correlation = data.corr(numeric_only=True)["SalePrice"].sort_values(ascending=False)
print("\nCorrelation with SalePrice:")
print(correlation.head(10))

# Step 4: Select features based on EDA
features = [
    "OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF",
    "1stFlrSF", "FullBath", "YearBuilt"
]
X = data[features]
y = data["SalePrice"]

# Step 5: Handle missing values
X = X.fillna(X.median())

# Step 6: Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Step 7: Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

# Step 9: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("\n----- Model Evaluation -----")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R²):", r2)

# Step 10: Predict price for a new house
new_house = pd.DataFrame({
    "OverallQual": [7], "GrLivArea": [2000], "GarageCars": [2],
    "TotalBsmtSF": [1000], "1stFlrSF": [1100], "FullBath": [2],
    "YearBuilt": [2005]
})
predicted_price = model.predict(new_house)
print("\n----- New House Prediction -----")
print("Predicted House Price:$", predicted_price[0])

# Step 11: Visualize actual vs predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
