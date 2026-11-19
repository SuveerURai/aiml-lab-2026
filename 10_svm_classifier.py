# Question: Demonstrate the working of an SVM classifier for a suitable dataset.
"""Train and evaluate a scaled linear SVM on the breast cancer dataset."""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def main():
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=1, stratify=data.target)
    model = make_pipeline(StandardScaler(), SVC(C=1.0, kernel="linear", random_state=1))
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predicted):.3f}")
    print(classification_report(y_test, predicted, target_names=data.target_names))
    print("Support vectors:", model[-1].n_support_.sum())
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, display_labels=data.target_names, cmap="Blues")
    plt.tight_layout(); plt.show()

if __name__ == "__main__": main()
