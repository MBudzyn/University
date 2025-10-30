import numpy as np
from matplotlib import pyplot as plt


def _sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))


class LogisticRegression:
    def __init__(self):
        self.X: np.array = None
        self.y = None
        self.theta = None
        self.learning_rate = 0.01
        self.epsilon = 1e-3

    def _update_gradients(self, X, y) -> None:
        m = len(y)
        predictions = _sigmoid(X @ self.theta)
        errors = predictions - y
        gradient = (X.T @ errors) / m
        self.theta -= self.learning_rate * gradient

    def fit(self, X, y):
        self.X = np.c_[np.ones(X.shape[0]), X]
        self.y = y
        self.theta = np.zeros(self.X.shape[1])
        previous_theta = self.theta.copy()
        while True:
            self._update_gradients(self.X, self.y)
            if np.linalg.norm(previous_theta - self.theta) < self.epsilon:
                break
            previous_theta = self.theta.copy()

    def predict(self, X):
        if X.ndim == 1:
            X = X.reshape(1, -1)

        X_with_bias = np.c_[np.ones(X.shape[0]), X]
        return 1 if _sigmoid(X_with_bias @ self.theta) >= 0.5 else 0


def generate_test_data(num_points=100, offset=2):
    x_class_0 = np.random.randn(num_points, 2) + np.array([-offset, -offset])
    x_class_1 = np.random.randn(num_points, 2) + np.array([offset, offset])

    X = np.vstack((x_class_0, x_class_1))
    y = np.hstack((np.zeros(num_points), np.ones(num_points)))

    plt.scatter(x_class_0[:, 0], x_class_0[:, 1], color='blue', label="Class 0")
    plt.scatter(x_class_1[:, 0], x_class_1[:, 1], color='red', label="Class 1")
    plt.legend()
    plt.title("Test Data for Logistic Regression")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

    return X, y


X, y = generate_test_data()
model = LogisticRegression()
model.fit(X, y)
print(model.predict(np.array([1, 1])))
print(model.predict(np.array([-1, -1])))
print(model.predict(np.array([0, 0])))
print(model.predict(np.array([2, 2])))
