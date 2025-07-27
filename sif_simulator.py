from linear_regression import SimpleLinearRegression, Parameter
from pandas import Series, DataFrame
import numpy as np


class SifSimulator:

    def simulate_sif(data_x, data_y, round=7):
        model = SimpleLinearRegression()
        sifs = []
        n = len(data_x)
        params1 = model.fit(data_x, data_y)
        for i in range(n):
            params2 = model.fit(
                SifSimulator._pseudo_normal_dataset(data_x, i),
                SifSimulator._pseudo_normal_dataset(data_y, i)
            )
            sifs.append(SifSimulator._compute_sif_values(params1, params2, n))
        return DataFrame(sifs, columns=["slope SIF", "intercept SIF"]).round(round)

    def _sample_influence_function(p1: float, p2: float, n):
        return (n - 1) * (p1 - p2)

    def _compute_sif_values(p1: Parameter, p2: Parameter, n: int) -> list:
        return [
            SifSimulator._sample_influence_function(p1.slope, p2.slope, n), 
            SifSimulator._sample_influence_function(p1.intercept, p2.intercept, n)
        ]

    def _pseudo_normal_dataset(s: Series, i: int) -> Series:
        """ Returns copied Series """
        return s.drop(s.index[i])