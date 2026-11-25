import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "telemetry/+/data"


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)
    print(f"Subscribed to: {MQTT_TOPIC}")


def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("\nReceived telemetry:")
    print(f"Topic: {message.topic}")
    print(f"Data: {payload}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)

print("MQTT ingestion service started...")
client.loop_forever()