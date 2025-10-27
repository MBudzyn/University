import pandas as pd
from data_view import DataView
from missing_filler import MissingFiller
from category_encoder import CategoryEncoder
from models_operations import Models


class HousePrices:
    def __init__(self):
        self.data = self.load_data("data/train.csv")
        self.test_data = self.load_data("data/test.csv")
        self.data_view = DataView(self.data)
        self.missing_filler = MissingFiller(self.data)
        self.category_encoder = CategoryEncoder(self.data)
        self.models = Models(self.data)

    def set_actual_data_to_objects(self):
        self.missing_filler.set_data(self.data)
        self.category_encoder.set_data(self.data)
        self.data_view.set_data(self.data)
        self.models.set_data(self.data)

    def preprocess_test_data(self) -> pd.DataFrame:
        missing_filler = MissingFiller(self.test_data)
        category_encoder = CategoryEncoder(self.test_data)
        missing_filler.execute()
        category_encoder.set_data(missing_filler.get_data())
        category_encoder.execute()
        return category_encoder.get_data()


    def get_data(self) -> pd.DataFrame:
        return self.data

    def set_data(self, data: pd.DataFrame) -> None:
        self.data = data

    def set_data_from_data_view(self) -> None:
        self.data = self.data_view.get_data()
        self.set_actual_data_to_objects()

    def set_data_from_missing_filler(self) -> None:
        self.data = self.missing_filler.get_data()
        self.set_actual_data_to_objects()

    def set_data_from_models(self) -> None:
        self.data = self.models.get_data()
        self.set_actual_data_to_objects()

    def set_data_from_category_encoder(self) -> None:
        self.data = self.category_encoder.get_data()
        self.set_actual_data_to_objects()

    def drop_columns(self, columns: list[str]) -> None:
        self.data = self.data.drop(columns, axis=1)
        self.set_actual_data_to_objects()

    def preprocess_data(self):
        self.missing_filler.execute()
        self.set_data_from_missing_filler()
        self.category_encoder.execute()
        self.set_data_from_category_encoder()

    def load_data(self, path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(path)
        except Exception as e:
            print(f"Error: {e}")


def main():
    H = HousePrices()
    H.data_view.print_data()
    H.preprocess_data()
    H.drop_columns(["Id", "GarageYrBlt"])
    H.models.RF_train_and_save(300, "models/RF_300.pkl")
    print(H.models.load_and_evaluate_RMSE("models/RF_300.pkl"))
    # H.data_view.print_data()
    # H.data_view.view_empty_values()
    # H.missing_filler.execute()
    # H.set_data_from_missing_filler()
    # H.category_encoder.execute()
    # H.set_data_from_category_encoder()
    # H.data_view.view_data_types(["object"])
    # H.data_view.count_columns()
    # H.data_view.print_corr()





if __name__ == "__main__":
    main()
