from google.cloud import pubsub_v1
import requests
import json

URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-12&orderby=time&limit=100'

r = requests.get(URL)
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('deportfolio-486507','earthquake-topic')

data = r.json()
for feature in data['features']:
    place = feature['properties']['place']
    mag = feature['properties']['mag']
    coord = feature['geometry']['coordinates']
    #print(f'Magnitude: {mag}, Place: {place}, Coordinates: {coord}')
    event = {
        'place': place,
        'magnitude': mag,
        'coordinates': coord
    }

    # Publish the event to Pub/Sub
    future = publisher.publish(topic_path, json.dumps(event).encode('utf-8'))
    future.result()  # Wait for the publish to complete
    print(f"Published message: {event}")




    

