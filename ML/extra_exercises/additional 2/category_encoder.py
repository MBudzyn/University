import pandas as pd
import category_encoders as ce


class CategoryEncoder:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def binary_encoding(self, columns: list[str]) -> None:
        encoder = ce.BinaryEncoder(cols=columns)
        self.data = encoder.fit_transform(self.data)

    def hot_ones_encoding(self, columns: list[str]) -> None:
        encoder = ce.OneHotEncoder(cols=columns, use_cat_names=True)
        self.data = encoder.fit_transform(self.data)

    def label_encoding(self, columns: list[str]) -> None:
        encoder = ce.OrdinalEncoder(cols=columns)
        self.data = encoder.fit_transform(self.data)

    def ordinal_encoding(self, column: str, mapping: dict) -> None:
        encoder = ce.OrdinalEncoder(cols=[column], mapping=[{'col': column, 'mapping': mapping}])
        self.data = encoder.fit_transform(self.data)

    def execute_hot_ones(self):
        self.hot_ones_encoding(["MSZoning", "Alley", "LandContour", "LotConfig", "LandSlope",
                                "Neighborhood", "Condition1", "Condition2", "BldgType", "HouseStyle",
                                "RoofStyle", "RoofMatl", "Exterior1st", "Exterior2nd", "MasVnrType", "Foundation",
                                "Heating", "Electrical", "Functional", "GarageType", "PavedDrive", "SaleType"
                                   , "SaleCondition", "MiscFeature"])

    def execute_ordinals(self):
        self.ordinal_encoding("Street", {"Grvl": 0, "Pave": 1})
        self.ordinal_encoding("LotShape", {"Reg": 3, "IR1": 2, "IR2": 1, "IR3": 0})
        self.ordinal_encoding("Utilities", {"AllPub": 0, "NoSeWa": 1})
        self.ordinal_encoding("ExterQual", {"Po": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4})
        self.ordinal_encoding("ExterCond", {"Po": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4})
        self.ordinal_encoding("BsmtQual", {"Unknown": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})
        self.ordinal_encoding("BsmtCond", {"Unknown": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})
        self.ordinal_encoding("BsmtExposure", {"Unknown": 0, "No": 1, "Mn": 2, "Av": 3, "Gd": 4})
        self.ordinal_encoding("HeatingQC", {"Po": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4})
        self.ordinal_encoding("CentralAir", {"N": 0, "Y": 1})
        self.ordinal_encoding("KitchenQual", {"Po": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4})
        self.ordinal_encoding("FireplaceQu", {"Unknown": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})
        self.ordinal_encoding("GarageFinish", {"Unknown": 0, "Unf": 1, "RFn": 2, "Fin": 3})
        self.ordinal_encoding("GarageQual", {"Unknown": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})
        self.ordinal_encoding("GarageCond", {"Unknown": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})
        self.ordinal_encoding("PoolQC", {"Unknown": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4})
        self.ordinal_encoding("Fence", {"Unknown": 0, "MnWw": 1, "GdWo": 2, "MnPrv": 3, "GdPrv": 4})
        self.ordinal_encoding("BsmtFinType1",
                              {"Unknown": 0, "Unf": 1, "LwQ": 2, "Rec": 3, "BLQ": 4, "ALQ": 5, "GLQ": 6})
        self.ordinal_encoding("BsmtFinType2",
                              {"Unknown": 0, "Unf": 1, "LwQ": 2, "Rec": 3, "BLQ": 4, "ALQ": 5, "GLQ": 6})

    def execute(self):
        self.execute_hot_ones()
        self.execute_ordinals()

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data



