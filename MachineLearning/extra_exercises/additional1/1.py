import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


data_directory = "netflix_titles.csv"


def ignore_first_space(obj):
    return str(obj).lstrip(" ")


def cut_to_first_space(obj):
    return str(obj).split(" ")[0]


class NetflixData:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = self.load_data()

    def load_data(self):
        return pd.read_csv(self.data_dir, low_memory=False, index_col=2)

    def empty_values_description(self):
        print("empty values in data")
        print(self.data.isnull().sum())
        print(f"sum of empty values in the data: {self.data.isnull().sum().sum()}")

    def view_listed_in(self):
        print("view listed in")
        print(self.data['listed_in'].unique())
        print(self.data['listed_in'].describe())
        print(self.data['listed_in'].value_counts())

    def view_type(self):
        print("view type")
        print(self.data['type'].unique())
        print(self.data['type'].describe())
        print(self.data['type'].value_counts())

    def view_date_added_format(self):
        print("view date added format")
        for data in self.data['date_added'].values:
            if len(str(data).split(" ")) > 3:
                print(str(data).split(" "), "length: ", len(str(data).split(" ")))

    def view_duration(self):
        print("view duration")
        print(self.data["movie duration"].unique())
        print(self.data['tv show duration'].unique())
        print(self.data['movie duration'].describe())
        print(self.data['tv show duration'].describe())

    def view_rating(self):
        print("view rating")
        print(self.data['rating'].unique())
        print(self.data['rating'].describe())
        print(self.data['rating'].value_counts())

    def data_description(self):
        print("data description")
        print(self.data.describe())
        print("data info")
        print(self.data.info())
        print("data head")
        print(self.data.head())
        self.empty_values_description()
        self.view_date_added_format()
        self.view_duration()
        self.view_rating()
        self.view_type()

    def drop_id(self):
        self.data.drop('show_id', axis=1, inplace=True)

    def parse_type_to_int(self):
        self.data['type'] = self.data['type'].map({'TV Show': 0, 'Movie': 1})

    def type_preprocessing(self):
        self.parse_type_to_int()

    def parse_date_added(self):
        self.data['date_added'] = self.data['date_added'].apply(ignore_first_space)
        self.data['date_added'] = pd.to_datetime(self.data['date_added'], format="%B %d, %Y")

    def fill_empty_date_added(self):
        self.data["date_added"] = self.data['date_added'].fillna(self.data['date_added'].mode()[0])

    def date_added_preprocessing(self):
        self.fill_empty_date_added()
        self.parse_date_added()

    def rating_preprocessing(self):
        self.set_wrong_ratings_to_none()
        self.fill_empty_rating()
        self.transform_rating()

    def set_wrong_ratings_to_none(self):
        # AFTER DURATION PREPROCESSING
        self.data.loc[self.data['rating'] == "84 min", 'rating'] = np.nan
        self.data.loc[self.data['rating'] == "74 min", 'rating'] = np.nan
        self.data.loc[self.data['rating'] == "66 min", 'rating'] = np.nan

    def fill_empty_rating(self):
        self.data["rating"] = self.data['rating'].fillna("No category")

    def transform_rating(self):
        transformer = OneHotEncoder(sparse_output=False)
        transformed_ratings = transformer.fit_transform(self.data['rating'].values.reshape(-1, 1))
        self.data['rating'] = list(transformed_ratings)
        self.data['rating'] = self.data['rating'].apply(lambda x: tuple(x))

    def fill_empty_duration(self):
        self.data["duration"] = self.data['duration'].fillna(self.data["rating"])

    def duration_split(self):
        self.data['movie duration'] = self.data['duration'].where(self.data['type'] == 1)
        self.data['tv show duration'] = self.data['duration'].where(self.data['type'] == 0)

    def duration_to_int(self):
        self.data['movie duration'] = self.data['movie duration'].dropna().apply(cut_to_first_space).astype(float)
        self.data['tv show duration'] = self.data['tv show duration'].dropna().apply(cut_to_first_space).astype(float)

    def duration_preprocessing(self):
        self.fill_empty_duration()
        self.duration_split()
        self.duration_to_int()

    def data_preprocessing(self):
        self.drop_id()
        self.type_preprocessing()
        self.date_added_preprocessing()
        self.duration_preprocessing()
        self.rating_preprocessing()


netflix_data = NetflixData(data_directory)
netflix_data.data_preprocessing()
netflix_data.view_listed_in()




