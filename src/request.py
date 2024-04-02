import os, json, googlemaps
from os.path import join

FRESH_REQ = False
cache_location = join(os.getcwd(), "cached_res.json")

if FRESH_REQ:
    with open(join(os.getcwd(), "keys.json")) as f:
        GMAPS_KEY = json.load(f)["places-key"]

    gmaps = googlemaps.Client(key=GMAPS_KEY)

    result = gmaps.places("restaurants in rochester city, NY, USA", type="restaurant")
    with open(cache_location, "w") as f:
        json.dump(result, f)
else:
    with open(cache_location, "r") as f:
        result = json.load(f)
        print(result)
