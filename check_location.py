from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="victo")

location = geolocator.geocode("郑州, China")
print((location.latitude, location.longitude))
print(location)
