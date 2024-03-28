import pandas as pd
import json
import os

from os.path import join


with open(join(os.getcwd(), "filepaths.json"), "r") as f:
    config = json.load(f)
nm = config["name-map"]
DATASET_FOLDER = config["raw-datasets"]
SAVE_FOLDER = join(DATASET_FOLDER, "cleaned")


def clean_census():
    raw_census_df = pd.read_excel(
        join(DATASET_FOLDER, nm["census"]),
        names=[
            "Geographic area",
            "April 1st 2020 population estimate",
            "July 1st 2020 population estimate",
            "July 1st 2021 population estimate",
            "July 1st 2022 population estimate",
        ],
    )

    raw_census_df.drop(index=0, inplace=True)
    raw_census_df["April 1st 2020 population estimate"] = pd.to_numeric(
        raw_census_df["April 1st 2020 population estimate"]
    )

    raw_census_df.to_csv(join(SAVE_FOLDER, "census.csv"), index=False)


if __name__ == "__main__":
    pass
