import requests

URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-12&orderby=time&limit=20'

r = requests.get(URL)
#print(r.json())

data = r.json()
for feature in data['features']:
    place = feature['properties']['place']
    mag = feature['properties']['mag']
    print(f'Magnitude: {mag}, Place: {place}')



    

