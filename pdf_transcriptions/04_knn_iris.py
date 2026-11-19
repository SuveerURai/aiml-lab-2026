# Question: Use K-Nearest Neighbor to classify Iris and print a confusion matrix.
# Transcribed from the manual; indentation restored for Python readability.
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

iris = datasets.load_iris()
print("Iris Dataset loaded...")
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)
# random_state=0
for i in range(len(iris.target_names)):
    print("Label", i, "-", str(iris.target_names[i]))

classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print("Results of Classification using K-nn with K=2")
for r in range(0, len(x_test)):
    print(" Sample:", str(x_test[r]), " Actual-label:", str(y_test[r]), "Predicted-label:", str(y_pred[r]))
print("ClassificationAccuracy:", classifier.score(x_test, y_test))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap="Blues", ax=plt.gca(), values_format='d')
plt.title("KNNClassificationConfusionMatrix", fontsize=14, fontweight='bold', pad=10)
plt.grid(False)
plt.show()
