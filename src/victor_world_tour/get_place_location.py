import os
import sys
import json
import time
import toml
import folium
import random

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="victor-world-tour-app")


def get_all_places():
    all_places_location = []
    data = toml.load(os.path.join(os.path.dirname(__file__), 'all_places_shown_on_map.toml'))
    for country, cities in data['all_places'].items():
        for city, score in cities.items():
            all_places_location.append(f"{city}, {country}")

    # read the database
    location_database_file = os.path.join(os.path.dirname(__file__), 'locations_database.json')
    if not os.path.exists(location_database_file):
        with open(location_database_file, "w") as f:
            f.write("")

    all_locations = {}
    with open(location_database_file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            place, location = line.split(":")
            all_locations[place] = location

        # print(json.dumps(all_locations, indent=4, ensure_ascii=False))

    return all_locations, all_places_location


def get_location(place_name):
    location = geolocator.geocode(place_name)
    return [location.latitude, location.longitude] if location else None


def get_all_locations():
    all_locations, all_places_location = get_all_places()

    for place in all_places_location:
        if place in all_locations and all_locations[place]:
            continue

        try_num = 1
        location = None
        while try_num < 4:
            try:
                location = get_location(place)
                break
            except Exception as e:
                print(f"Error: {e}")
                try_num += 1

                if try_num == 4:
                    location = None
                    print(f'Failed to get location for {place}')
                    break
            time.sleep(random.randint(2, 4))

        # save to json file
        with open(os.path.join(os.path.dirname(__file__), 'locations_database.json'), "a") as f:
            f.write(f"{place}:{location}")
            f.write("\n")

        print(f"{place}:{location} added to {os.path.join(os.path.dirname(__file__), 'locations_database.json')}")


if __name__ == "__main__":
    # get_all_places()
    get_all_locations()
    # print("All locations added to locations_database.json")
    # print("Done")
