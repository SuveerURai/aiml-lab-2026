# Question: Apply EM to cluster a CSV dataset, compare with k-Means, and comment on cluster quality.
"""Compare Gaussian-mixture EM and k-Means on the bundled Iris dataset."""
from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score, silhouette_score

def main():
    iris = load_iris()
    X = StandardScaler().fit_transform(iris.data)
    em = GaussianMixture(n_components=3, random_state=42).fit_predict(X)
    km = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X)
    for name, labels in (("EM (Gaussian mixture)", em), ("k-Means", km)):
        print(f"{name}: silhouette={silhouette_score(X, labels):.3f}, adjusted Rand={adjusted_rand_score(iris.target, labels):.3f}")
    print("Higher silhouette indicates more separated clusters; adjusted Rand compares clusters with known Iris species.")

if __name__ == "__main__": main()
