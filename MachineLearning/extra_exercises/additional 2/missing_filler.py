
import pandas as pd


class MissingFiller:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def get_data(self) -> pd.DataFrame:
        return self.data

    def fill_empty_values(self, columns: str, value: str = "Unknown") -> None:
        self.data[columns] = self.data[columns].fillna(value)

    def drop_empty_values(self, columns: list[str]) -> None:
        self.data = self.data.dropna(subset=columns)

    def fill_empty_median(self, columns: list[str]) -> None:
        for column in columns:
            self.data[column] = self.data[column].fillna(self.data[column].median())

    def fill_empty_columns(self, columns: list[str], value: str = "Unknown") -> None:
        for column in columns:
            self.fill_empty_values(column, value)

    def fill_empty_mode(self, columns: list[str]) -> None:
        for column in columns:
            mode_value = self.data[column].mode()[0]
            self.data.loc[:, column] = self.data[column].fillna(mode_value)

    def empty_values_info(self) -> None:
        print(self.data.isnull().sum()[self.data.isnull().sum() > 0])

    def execute(self):
        self.fill_empty_columns(["MasVnrType", "BsmtQual", "PoolQC", "GarageCond", "GarageQual", "GarageType"
                                 , "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2", "Alley", "MiscFeature"
                                 , "Fence", "FireplaceQu", "GarageYrBlt", "GarageFinish", ])
        self.fill_empty_median(["MasVnrArea", "LotFrontage"])
        self.drop_empty_values(["Electrical"])

    def set_data(self, data):
        self.data = data


def main():
    pass


if __name__ == "__main__":
    main()

