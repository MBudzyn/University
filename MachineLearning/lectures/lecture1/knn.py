import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


class KNearestNeighbours:
    def __init__(self, k):
        self.k = k
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, x_to_predict):
        distances = np.linalg.norm(self.X - x_to_predict, axis=1)
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_labels = self.y[nearest_indices]
        return Counter(nearest_labels).most_common(1)[0][0]


class ClustersGenerator:

    def __init__(self, n_clusters, n_samples, n_features):
        self.n_clusters = n_clusters
        self.n_samples = n_samples
        self.n_features = n_features
        self.X = None
        self.y = None

    def generate(self):
        X = []
        y = []
        for i in range(self.n_clusters):
            X.append(np.random.randn(self.n_samples, self.n_features)/5 + i)
            y.append(np.full(self.n_samples, i))
        self.X = np.concatenate(X)
        self.y = np.concatenate(y)
        return self.X, self.y

    def plot(self):
        plt.scatter(self.X[:, 0], self.X[:, 1], c=self.y, cmap='viridis')
        plt.show()


generator = ClustersGenerator(3, 100, 2)
X, y = generator.generate()

model = KNearestNeighbours(3)
model.fit(X, y)
new_data = np.array([[0, 0], [1, 1], [2, 2], [3, 3],[0,0.5],[1,1.5],[2,2.5],[3,3.5],[0.5,0],[1.5,1]])
predictions = [model.predict(x) for x in new_data]
plt.scatter(X[:, 0], X[:, 1], c=y,s=5, cmap='viridis')
plt.scatter(new_data[:, 0], new_data[:, 1], c=predictions,s = 100, cmap="viridis", marker='x')
plt.show()

