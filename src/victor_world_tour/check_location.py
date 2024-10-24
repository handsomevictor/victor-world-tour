"""
This script uses the geopy library to get the latitude and longitude of a location using the Nominatim geocoder.
"""

from geopy.geocoders import Nominatim


if __name__ == '__main__':
    geolocator = Nominatim(user_agent="victor-world-tour-app")

    location = geolocator.geocode("郑州, China")

    print((location.latitude, location.longitude))
    print(location)

