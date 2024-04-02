import os, operator

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from helpers import census_df


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
        except KeyError as e:
            raise StopIteration
        return self.current


def get_cumulative_cutoff(cumulative_vals, desired_prop=0.8):
    """returns the index `rank` which captures at least the `desired_prop` of total values"""
    assert 0 <= desired_prop < 1, "desired_prop should be in [0,1)"
    ys = np.array(list(cumulative_vals))
    proportions = ys / ys[-1]
    assert np.isclose(
        proportions[-1], 1.0
    ), f"The final captured propotion should be 1, but is {proportions[-1]}"
    return proportions, np.where(proportions > desired_prop)[0][0]


def plot_cumulative_pop(desired_prop=0.8):
    assert 0 <= desired_prop < 1, "desired_prop should be in [0,1)"
    df = census_df[["Jul. 1 2022 pop. est."]].rename(
        columns={"Jul. 1 2022 pop. est.": "Population"}
    )
    xs = df.index
    ys, cutoff = get_cumulative_cutoff(CumulativeCol(df["Population"]), desired_prop)

    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    fig.title = "Cumulative Population vs City Population Rank"
    fig.xlabel = "City Population Rank"
    fig.ylabel = "Cumulative Population"

    ax.axhline(y=desired_prop, c="green", ls="--")
    ax.axvline(x=cutoff, c="red", ls="--")
    print(cutoff)
    plt.show()


if __name__ == "__main__":
    plot_cumulative_pop()
