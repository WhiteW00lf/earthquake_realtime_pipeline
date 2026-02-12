from google.cloud import pubsub_v1
import requests
import json

URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-12&orderby=time&limit=20'

r = requests.get(URL)
topic = 'projects/deportfolio-486507/topics/earthquake-topic'
subs = 'projects/deportfolio-486507/subscriptions/earthquake_sub'
#print(r.json())

data = r.json()
for feature in data['features']:
    place = feature['properties']['place']
    mag = feature['properties']['mag']
    coord = feature['geometry']['coordinates']
    print(f'Magnitude: {mag}, Place: {place}, Coordinates: {coord}')
    event = {
        'place': place,
        'magnitude': mag,
        'coordinates': coord
    }

    # Publish the event to Pub/Sub
    publisher = pubsub_v1.PublisherClient(topic, subs, json.dumps(event).encode('utf-8'))

    


    

