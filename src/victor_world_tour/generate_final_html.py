import os
import json
import math
import toml
import folium


def generate_map_html(html_name="my_travel_map.html"):
    location_database_file = os.path.join(os.path.dirname(__file__), 'locations_database.json')
    all_places_long_lat = toml.load(os.path.join(os.path.dirname(__file__), 'all_places_shown_on_map.toml'))

    all_locations = {}
    with open(location_database_file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            place, location = line.split(":")
            all_locations[place] = eval(location)
            # make sure the location format is correct: "[48.8588897, 2.3200410217200766]"

    # create map
    m = folium.Map(location=[20, 0], zoom_start=2)
    scale_factor = 15000  # change this value to control the size of the circle

    for place, location in all_locations.items():
        city, country = place.split(", ")
        folium.Circle(
            location=location,  # list of latitude and longitude
            radius=scale_factor * (math.sqrt(all_places_long_lat['all_places'][country][city]) * 2),
            color='green',  # 圆圈颜色
            fill=True,  # 填充
            fill_color='lightblue',  # 填充颜色
            fill_opacity=0.3,  # 透明度（0-1之间）
            popup=f"{city}, {country}"
        ).add_to(m)

        # 颜色深，表示呆的时间久？
        # 用自定义笑脸和哭脸？

    map_file = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', html_name)
    m.save(map_file)
    print(f"Map saved to /docs/{html_name}")


if __name__ == "__main__":
    generate_map_html()
