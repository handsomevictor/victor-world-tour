import time
import json
import random
import folium
from geopy.geocoders import Nominatim

from resources import all_places

all_places_location = []
for country, cities in all_places.items():
    for city, score in cities.items():
        all_places_location.append(f"{city}, {country}")

geolocator = Nominatim(user_agent="victor-world-tour-app")

# read the database
all_locations = {}
with open("locations_database.json", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        place, location = line.split(":")
        all_locations[place] = location

    print(json.dumps(all_locations, indent=4, ensure_ascii=False))


# 函数：根据地名获取经纬度
def get_location(place_name):
    location = geolocator.geocode(place_name)
    return [location.latitude, location.longitude] if location else None


def get_all_locations():
    # 循环通过地名获取经纬度并添加标记
    for place in all_places_location:
        # check if location already exists
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
        with open("locations_database.json", "a") as f:
            f.write(f"{place}:{location}")
            f.write("\n")

        print(f"{place}: {location} added to locations_database.json")


if __name__ == "__main__":
    get_all_locations()
    print("All locations added to locations_database.json")
    print("Done")
