import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DataView:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def view_data_types(self, data_types: list[str]) -> None:
        for col in self.data.select_dtypes(include=data_types).columns:
            print(f"{col}: {self.data[col].dtype}")

    def view_columns_head(self, columns: list[str]) -> None:
        print(self.data[columns].head())

    def view_empty_values(self) -> None:
        print(self.data.isnull().sum()[self.data.isnull().sum() > 0])

    def value_counts_plot(self, column: str) -> None:
        value_counts = self.data[column].value_counts()
        ax = value_counts.plot(kind="bar")
        plt.title(f"{column} value counts")
        plt.xlabel(column)
        plt.ylabel("Count")

        for i, count in enumerate(value_counts):
            ax.text(i, count + 0.1, str(count), ha='center', va='bottom')

        plt.show()

    def view_value_counts(self, column: str) -> None:
        print(self.data[column].value_counts())


    def print_data(self) -> None:
        print(f"head: {self.data.head()}")
        print(f"info: {self.data.info()}")
        print(f"describe: {self.data.describe()}")

    def print_corr(self) -> None:
        data = self.data.select_dtypes(include=[np.int64,np.float64])
        try:
            data = data.corrwith(self.data["SalePrice"])
            positive_corr = data[data > 0]
            negative_corr = data[data < 0]
            positive_corr = positive_corr.sort_values(ascending=False)
            negative_corr = negative_corr.sort_values(ascending=True)
            print("Positive correlation: ")
            for key, value in positive_corr.items():
                print(f"{key}: {value}")

            print("Negative correlation: ")
            for key, value in negative_corr.items():
                print(f"{key}: {value}")
        except KeyError:
            print("Column 'SalePrice' not found in data.")

    def draw_histogram(self) -> None:
        self.data.hist(bins=50, figsize=(20, 15))
        plt.show()

    def count_columns(self) -> None:
        print("number of columns: ", len(self.data.columns))

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


def main():
    pass


if __name__ == "__main__":
    main()
