import phonenumbers
import folium
from phonenumbers import carrier
from phonetest import number
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
key = "2111461f9cd643f79a185641edb10361"
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, "en")
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_Start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)
myMap.save("myLocation.html")