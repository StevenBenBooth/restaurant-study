import os, json
from os.path import join

from eda import get_cumulative_cutoff
from helpers import census_df, gmaps


cache_location = join(os.getcwd(), "cached_res.json")
CACHE = False


def make_request(location):
    result = gmaps.places(f"restaurants in {location}", type="restaurant")
    if CACHE:
        with open(cache_location, "w") as f:
            json.dump(result, f)
    return result


def multi_request(num):
    names = census_df[["Geographic area"]].iloc[:num]
    print(names)


if __name__ == "__main__":
    multi_request(num=100)
