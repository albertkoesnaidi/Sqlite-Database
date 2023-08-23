from geopy.geocoders import Nominatim
gc=Nominatim(user_agent='http')
loc=gc.geocode("darmo harapan regency")
print(loc.latitude, loc.longitude)