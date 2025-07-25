import pandas as pd
import numpy as np
from dataclasses import dataclass



def select_column(df: pd.DataFrame, i: int) -> pd.Series:
    return df.iloc[:, i]


@dataclass
class Answer:
    maharanobis: np.ndarray[np.float32]

class AssignmentData:

    def __init__(self, path: str):
        self._df = self.__load_data(path)

    def get_data(self):
        return self._df.iloc[:, :2]
    
    def answer_sif_in_slope(self):
        return select_column(self._df, 2)
    
    def answer_sif_in_intercept(self):
        return select_column(self._df, 3)
    
    def answer_maharanobis(self):
        return select_column(self._df, 4)
    
    def __load_data(self, path: str) -> pd.DataFrame:
        df = pd.read_csv(path, encoding='cp932')
        df.set_index(df.columns[0], inplace=True)
        return df


# Test
if __name__ == "__main__":
    path = "./data/students_height_and_sitting_height.csv"
    data = AssignmentData(path)
    print(f"データ：{data.get_data()}")
    print(f"傾きのSIF：{data.answer_sif_in_slope()}")
    print(f"切片のSIF{data.answer_sif_in_intercept()}")
    print(f"マハラノビスの距離：{data.answer_maharanobis()}")