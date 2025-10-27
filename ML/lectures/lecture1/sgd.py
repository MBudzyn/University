import numpy as np
from random import randint
from matplotlib import pyplot as plt

class SGD:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.theta: np.array = None
        self.epsilon = 1e-3
        self.X = None
        self.y = None

    def _compute_gradient(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        random_index = randint(0, X.shape[0] - 1)
        return 2 * X[random_index] * (X[random_index] @ self.theta - y[random_index])

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.X = np.c_[np.ones(X.shape[0]), X]
        self.y = y
        self.theta = np.random.randn(self.X.shape[1])

        while True:
            gradient = self._compute_gradient(self.X, self.y)
            if np.linalg.norm(gradient) < self.epsilon:
                break
            self.theta = self.theta - self.learning_rate * gradient

    def predict(self, X: np.ndarray) -> np.ndarray:
        X_with_bias = np.c_[np.ones(X.shape[0]), X]
        return X_with_bias @ self.theta

    def plot(self):
        plt.scatter(self.X[:, 1], self.y, label='Dane', color='blue')
        plt.plot(self.X[:, 1], self.predict(self.X[:, 1]), color='red', label='Regresja')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Wykres SGD")
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.legend()
        plt.show()




