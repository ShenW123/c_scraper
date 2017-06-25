from googleplaces import GooglePlaces, types, lang
import googlemaps
from datetime import datetime
import json
from settings import WORKPLACE, DOWNTOWN

with open('auth_gmaps.json') as data_file:
    gmaps_auth = json.load(data_file)

YOUR_API_KEY = gmaps_auth['key']
gmaps = googlemaps.Client(key=YOUR_API_KEY)

def findDistanceDuration(startplace, endplace):
	transit = {}
	now = datetime.now()
	directions_result = gmaps.directions(startplace,
                                     endplace,
                                     mode="transit",
                                     departure_time=now)
	transit['duration'] = directions_result[0]['legs'][0]['duration']['text']
	transit['distance'] = directions_result[0]['legs'][0]['distance']['text']
	return transit

def locationService(geotag):
	searchplace = {
		"lat": geotag[0],
		"lng": geotag[1]
	}
	work = findDistanceDuration(searchplace, WORKPLACE)
	dt = findDistanceDuration(searchplace, DOWNTOWN)
	return {"work": work, "dt": dt}

