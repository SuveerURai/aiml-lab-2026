# Question: Use a Python library to classify Iris with KNN and print a confusion matrix.
"""K-nearest neighbors classification on the Iris dataset."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt

def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42, stratify=iris.target)
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    print("Accuracy:", round(accuracy_score(y_test, prediction), 3))
    print("Confusion matrix:\n", confusion_matrix(y_test, prediction))
    ConfusionMatrixDisplay.from_predictions(y_test, prediction, display_labels=iris.target_names, cmap="Blues")
    plt.tight_layout(); plt.show()

if __name__ == "__main__": main()
