# Question: Demonstrate the working SVM classifier for a suitable dataset.
# Transcribed from the manual; indentation restored for Python readability.
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Load dataset
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target

# Reserve the last sample as unseen data
new_instance = X[-1:]
new_actual = y[-1]
X = X[:-1]
y = y[:-1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y
)

# Standardize features
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Train SVM Model
svc = SVC(C=1.0, kernel="linear", random_state=1)
svc.fit(X_train_std, y_train)

# Model Evaluation Predictions
y_predict = svc.predict(X_test_std)
print("=== Model Evaluation ===")
print("Accuracy score:%.3f" % metrics.accuracy_score(y_test, y_predict))

# Plot confusion matrix
disp = metrics.ConfusionMatrixDisplay.from_estimator(
    svc,
    X_test_std,
    y_test,
    display_labels=bc.target_names,
    cmap=plt.cm.Blues,
)
disp.ax_.set_title("SVM Classification Confusion Matrix", fontweight="bold", fontsize=14, pad=12)
plt.show()

print("\nClassification Report:")
print(metrics.classification_report(y_test, y_predict, target_names=bc.target_names))
print("Total Support Vectors:", len(svc.support_))

# Predict on the single unseen instance (with scaling fix)
new_instance_std = sc.transform(new_instance)
prediction = svc.predict(new_instance_std)
print("\n=== Classification of One Unseen Instance ===")
print("Predicted class:", bc.target_names[prediction[0]])
print("Actual class:", bc.target_names[new_actual])
