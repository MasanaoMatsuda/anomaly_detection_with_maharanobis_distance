import numpy as np
from pandas import Series
from sklearn.linear_model import LinearRegression
from dataclasses import dataclass


@dataclass
class Parameter:
   slope: np.float64
   intercept: np.float64

   def __str__(self):
       return f"傾き: {self.slope} / 切片: {self.intercept}"

   
def extended_linspace(x: Series, ratio: float = 0.05, num: int = 100) -> np.ndarray:
    x_min = x.min() * (1 - ratio)
    x_max = x.max() * (1 + ratio)
    return np.linspace(x_min, x_max, num)


class SimpleLinearRegression:

    def __init__(self):
        self.model = LinearRegression()

    def fit(self, x: Series, y: Series) -> Parameter:
        self.model.fit(x.values.reshape(-1, 1), y.values)
        return Parameter(
            self.model.coef_[0], 
            self.model.intercept_
        )

    def predict(self, x: Series):
        return self.model.predict(x.values.reshape(-1, 1))