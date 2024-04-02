import os, operator

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from clean_helpers import config, nm


# TODO: refactor; this is just a fold iterator
class CumulativeCol:
    def __init__(self, column, initial_val=0, agg_fun=operator.add):
        """`fun` is a binary operator that combines the current aggregated value an element of `column`
        `column` should be a one-dimensional, indexible data container
        `initial_val` should be of the column dtype, and both should be the datatype accepted by `fun`
        """
        # TODO: implement type check for column
        self.values = column
        self.current = initial_val
        self.agg_fun = agg_fun
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.current = self.agg_fun(self.current, self.values[self.index])
            self.index += 1
        except IndexError as e:
            raise StopIteration
        return self.current


def plot_cumulative_pop():
    cleaned_path = os.path.join(config["raw-datasets"], nm["census"]["cleaned"])
    df = pd.read_csv(cleaned_path, usecols=["Jul. 1 2022 pop. est."])
    df.columns = ["Population"]
    xs = df.index
    ys = CumulativeCol(df["Population"])
    ys = ys.values / df["Population"].sum()
    print(ys)
    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    fig.title = "Cumulative Population vs City Population Rank"
    fig.xlabel = "City Population Rank"
    fig.ylabel = "Cumulative Population"
    ax.axhline(y=0.8)

    fig.show()


if __name__ == "__main__":
    plot_cumulative_pop()