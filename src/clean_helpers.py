import pandas as pd
import json
import os

from os.path import join


def get_config():
    with open(join(os.getcwd(), "filepaths.json"), "r") as f:
        config = json.load(f)
    return config


config = get_config()
nm = config["name-map"]
DATASET_FOLDER = config["raw-datasets"]


def clean_census():
    raw_name, save_name = nm["census"]["raw"], nm["census"]["cleaned"]
    raw_census_df = pd.read_excel(
        join(DATASET_FOLDER, raw_name),
        names=[
            "Geographic area",
            "Apr. 1 2020 pop. est.",
            "Jul. 1 2020 pop. est.",
            "Jul. 1 2021 pop. est.",
            "Jul. 1 2022 pop. est.",
        ],
    )

    raw_census_df.drop(index=0, inplace=True)
    raw_census_df["Apr. 1 2020 pop. est."] = pd.to_numeric(
        raw_census_df["Apr. 1 2020 pop. est."]
    )
    raw_census_df.sort_values(by="Jul. 1 2022 pop. est.", ascending=False, inplace=True)
    raw_census_df.to_csv(join(DATASET_FOLDER, save_name), index=False)


if __name__ == "__main__":
    clean_census()
