import os, json
from os.path import join

from eda import get_cumulative_cutoff
from helpers import census_df, gmaps
import time

CACHE = True
WAIT_TIME = 2


def extract_restaurant_info():
    """What do I want from each restaurant? What to save?"""
    pass


def location_restaurants(location):
    location_query = f"restaurants in {location}"
    results_list, next_page_token = single_request(location_query)
    # TODO: UH OH! I am limited to 60 locations per request...
    # Try https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.find_place instead
    # I am already getting data I don't need.
    
    while next_page_token:
        time.sleep(WAIT_TIME)

        print(next_page_token + "\n")
        new_results, next_page_token = single_request(location_query, next_page_token)
        results_list.extend(new_results)

    if CACHE:
        with open(
            join(os.getcwd(), "cached_location_res", f"{location}.json"), "w"
        ) as f:
            json.dump(results_list, f)

    return results_list


def single_request(query, page_token=None):
    # TODO: put the type="restaurant" into the call signature somehow
    response = gmaps.places(query, type="restaurant", page_token=page_token)

    results_list = response["results"]
    try:
        next_page_token = response["next_page_token"]
    except KeyError:
        next_page_token = None

    return results_list, next_page_token


def top_cities_request(num):
    names = census_df[["Geographic area"]].iloc[:num]
    print(names)


if __name__ == "__main__":
    print(location_restaurants("New York City, NY, USA"))
    # top_cities_request(num=100)
