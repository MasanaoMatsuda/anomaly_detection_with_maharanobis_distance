from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from linear_regression import SimpleLinearRegression, extended_linspace


class Drawer:

    def __init__(self, df: DataFrame, fontsize=9):
        self.x = df.iloc[:, 0]
        self.y = df.iloc[:, 1]
        self.size = len(df)
        self.x_label = df.columns[0]
        self.y_label = df.columns[1]
        self.fontsize = fontsize


    def plot_scatter_with_index(self, title: str):
        plt.scatter(self.x, self.y)
        # 各点にインデックスを表示
        for i in range(self.size):
            plt.text(self.x.iloc[i], self.y.iloc[i], str(i+1), 
                    fontsize=self.fontsize, ha='right', va='bottom')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.show()


    def plot_scatter_with_regression_line(self, model: SimpleLinearRegression, x: Series, title: str):
        x = extended_linspace(x, ratio=0.01)
        y = model.predict(Series(x))
        plt.scatter(self.x, self.y)
        # 各点にインデックスを表示
        for i in range(self.size):
            plt.text(self.x.iloc[i], self.y.iloc[i], str(i+1), 
                    fontsize=self.fontsize, ha='right', va='bottom')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.plot(x, y, color='red', label='Regression Line')
        plt.legend()
        plt.show()

    def plot(self, vals):
        plt.scatter(vals[:,0], vals[:,1])
        plt.show()



class TableVisualizer:

    def print_result_table(sifs: DataFrame, scores: list, round: int):
        _df = DataFrame(
            sifs.values, 
            index=range(1,len(sifs)+1),
            columns=sifs.columns
        )
        _df["score"] = scores
        print(_df.round(round))