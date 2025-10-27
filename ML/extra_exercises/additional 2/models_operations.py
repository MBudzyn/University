
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt


class Models:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.train_X = None
        self.test_X = None
        self.train_y = None
        self.test_y = None
        self.split_data("SalePrice")

    def split_data(self, target, test_size: float = 0.2) -> None:
        self.train_X, self.test_X, self.train_y, self.test_y = train_test_split(self.data.drop(target, axis=1),
                                                                                self.data[target], test_size=test_size,
                                                                                random_state=42)

    def set_test_data(self, test_X):
        self.test_X = test_X


    def RF_train_and_save(self, n_estimators: int, path: str) -> None:
        self.split_data("SalePrice")
        model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
        model.fit(self.train_X, self.train_y)
        self.save_model(model, path)

    def load_and_evaluate_RMSE(self, path: str):
        model = self.get_model_from_path(path)
        predictions = model.predict(self.test_X)
        return root_mean_squared_error(self.test_y, predictions)

    def RF_train_and_evaluate_return_RMSE(self, n_estimators: int) -> float:
        model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
        model.fit(self.train_X, self.train_y)
        predictions = model.predict(self.test_X)
        return root_mean_squared_error(self.test_y, predictions)

    def save_model(self, model, path: str) -> None:
        import joblib
        joblib.dump(model, path)

    def get_model_from_path(self, path: str):
        import joblib
        return joblib.load(path)

    def execute(self, rng: int = 300):
        self.train_number_of_models(rng)

    def train_number_of_models(self, rng: int = 300):
        rmse_scores = {}
        for i in range(50, rng):
            print(i)
            rmse = self.RF_train_and_evaluate_return_RMSE(i)
            rmse_scores[i] = rmse

        self.plot_stabilizing_rmse(rmse_scores)

    def plot_stabilizing_rmse(self, results):
        plt.figure(figsize=(10, 6))
        x = [i for i in results.keys()]
        y = [i for i in results.values()]
        plt.plot(x, y)
        plt.xlabel("Model")
        plt.ylabel("RMSE")
        plt.title("Model Performance Comparison (Regression)")
        plt.xticks(rotation=45, ha="right")
        plt.savefig("rmse metric of different numbers of trees", format="png", dpi=300)
        plt.tight_layout()
        plt.show()

    def print_info_test_and_train(self):
        print(f"shape: {self.data.shape}")
        print(f"shape train_X: {self.train_X.shape}")
        print(f"shape test_X: {self.test_X.shape}")
        print(f"shape train_y: {self.train_y.shape}")
        print(f"shape test_y: {self.test_y.shape}")
        print(f"Train X: {self.train_X}")
        print(f"Test X: {self.test_X}")
        print(f"Train y: {self.train_y}")
        print(f"Test y: {self.test_y}")

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


