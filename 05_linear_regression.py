# Question: Demonstrate linear regression on a suitable dataset and predict an output.
"""Linear regression using scikit-learn's built-in diabetes dataset."""
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def main():
    data = load_diabetes(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    predicted = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, predicted):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, predicted)):.2f}")
    print(f"R-squared: {r2_score(y_test, predicted):.3f}")
    sample = X_test.iloc[[0]]
    print("Predicted target for first test sample:", round(model.predict(sample)[0], 2))

if __name__ == "__main__": main()
