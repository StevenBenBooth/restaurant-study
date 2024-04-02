from clean_helpers import config, nm
import os
import pandas as pd
import googlemaps
import json

cleaned_path = os.path.join(config["raw-datasets"], nm["census"]["cleaned"])
census_df = pd.read_csv(cleaned_path)

with open(os.path.join(os.getcwd(), "keys.json")) as f:
    GMAPS_KEY = json.load(f)["places-key"]
gmaps = googlemaps.Client(key=GMAPS_KEY)
