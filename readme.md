# Interactive Map to Show All the places that Victor has been to

## Author

**[Handsome Victor](https://zhenning-li.com)**

## Aim

To make a map that records Victor's existence in the world

## How to Run

Directly run the [run.py](run.py) script:

1. Clond this project by running: `git clone https://github.com/handsomevictor/victor-world-tour.git`
2. `cd` to this project: `cd victor-world-tour`
3. Install the dependencies: `pip install -r requirements.txt` or `pip3 install -r requirements.txt` or use
   `uv install` if you love this RUST style management tool
4. execute: `python run.py` or `python3 run.py`

## How to Make Your Own Map

1. Add your own places to the [all_places_shown_on_map.toml](src/victor_world_tour/all_places_shown_on_map.toml),
   remember to follow the format (if you don't want to give a scroe, put a 0)
2. After adding your places, run the [run.py](run.py) script but have to change the param: `update_all_locations=True`
   in main(), to let geolocator to add the location of the places that are not in the database yet
3. After it's done, you will find your own map in html format here [my_travel_map.html](docs/my_travel_map.html)

## Script Logic

1. This [all_places_shown_on_map.toml](src/victor_world_tour/all_places_shown_on_map.toml) toml file records all the
   places that Victor has been to, and the score of each place
2. This [get_place_location.py](src/victor_world_tour/get_place_location.py) script will go through the toml file and
   get the location of each place using geopy.geocoders.Nominatim if the location is not in
   [locations_database.json](src/victor_world_tour/locations_database.json) yet
3. This [generate_final_html.py](src/victor_world_tour/generate_final_html.py) script will use `folium` to generate the
   final html file that shows all the places on the map

## Reminders

1. When using `geolocator.geocode` to get the location of a place, it is not always accurate. You can use
   [check_location.py](src/victor_world_tour/check_location.py) to check if the location you want to input can
   return anything. A reminder is, this `geolocator` supports more than one language, so for example if you want to
   get the location of `Zhengzhou` (in Henan province), you will find `Zhengzhou, China` is not in Henan due to
   collation issue, you can use `郑州` instead of `Zhengzhou` to get it correct. When the result is wrong, it returns
   None or a false location
2. When running [get_place_location.py](src/victor_world_tour/get_place_location.py) / using `geolocator.geocode`,
   due to the API setting, sometimes it will return an Error. I already implemented a retry and sleep mechanism,
   but if in your web environment, you can't get the location of some places after many trials, you can try to use
   some other websites / modules like `Geopy`, `Geocoder`, `Google Maps API`, etc.

## Future Possible Enhancement

- Add photos of places to the map (when moving the mouse over the marker or clicking on it)
- Deploy on a website and add multiple dropdowns to see different categories of the results
- Utilize more functions in `geopy` to see what other interesting stuff can be done. It supports very details location
  like a university name, or it can also do reverse geocoding: given a location, find the address - example:

```python
geolocator.reverse("48.8566, 2.3522")

# Output:
# Hôtel de Ville, Place de l'Hôtel de Ville, Quartier Saint-Merri, Paris 4e Arrondissement, Paris, Île-de-France, 
# France métropolitaine, 75004, France
```

- Use folium and government / non-official world commerce trade data, to show how trade is distributed around the world,
  and possibly to give a score of most countries their dependency on some certain conmmodities.

## License

This project is GNU GENERAL PUBLIC Version 3 licensed - see the [LICENSE](LICENSE) file for details

## Version

Current version: **1.0.1**

### Updates

- **[2024-10-25]** Changed all structures to use `uv` to manage the dependencies (yes I am RUST fan),
  added a `requirements.txt` file, added LICENSE file


