from typing import List
import numpy as np
import matplotlib.pyplot as plt
from sgd import SGD


class LinearRegression:
    def __init__(self):
        self.X = None
        self.y = None
        self.theta = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.X = np.c_[np.ones(X.shape[0]), X]
        self.y = y
        self.theta = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.y

    def predict(self, X: np.ndarray) -> np.ndarray:
        X_with_bias = np.c_[np.ones(X.shape[0]), X]
        return X_with_bias @ self.theta

    def plot(self):
        plt.scatter(self.X[:, 1], self.y, label='Dane', color='blue')
        plt.plot(self.X[:, 1], self.predict(self.X[:, 1]), color='red', label='Regresja')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Wykres regresji liniowej")
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.legend()
        plt.show()


def linear_data_generator(n: int, a: float, b: float) -> tuple:
    X = []
    y = []
    for i in range(n):
        X.append(np.random.rand(1))
        y.append(a * X[i] + b + np.random.randn(1)/5)

    return np.array(X).flatten(), np.array(y).flatten()


X, y = linear_data_generator(100, 2, 3)

model2 = SGD(0.01)
model = LinearRegression()
model2.fit(X, y)
model.fit(X, y)

model2.plot()
model.plot()

