from google.cloud import pubsub_v1
import json

PROJECT_ID = "deportfolio-486507"
SUBSCRIPTION_ID = "earthquake_sub"

subscriber = pubsub_v1.SubscriberClient()
subscriber_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def getmessage(message):
    try:
        data = json.loads(message.data.decode('utf-8'))
        print(f"Received message: {data}")

        magnitude = data.get("magnitude", 0)
        place = data.get("place", "Unknown location")

        if magnitude >= 5.0:
            print(f"🚨 Significant earthquake: {magnitude} at {place}")

        message.ack()

    except Exception as e:
        print("Error processing message:", e)
        message.nack()

streaming_pull_future = subscriber.subscribe(
    subscriber_path,
    callback=getmessage
)

print(f"Listening for messages on {subscriber_path}...")

try:
    streaming_pull_future.result()
    print("Pull successful")
except KeyboardInterrupt:
    streaming_pull_future.cancel()
