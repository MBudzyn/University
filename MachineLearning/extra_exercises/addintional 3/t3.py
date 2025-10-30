import pandas as pd
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split


class Cars:
    def __init__(self):
        self.data = pd.read_csv('data/CarPrice_Assignment.csv')
        self.test_size = 0.2
        self.trainX, self.trainY, self.testX, self.testY =(
            train_test_split(self.data.drop('price', axis=1), self.data['price'],
                             test_size=self.test_size, random_state=42))

    def preprocessing(self):
        pass



    def head(self):
        return self.data.head()


C = Cars()
print(C.trainX.head())
print(C.trainY.head())
print(C.testX.head())
print(C.testY.head())



