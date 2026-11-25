import json
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "telemetry/+/data"


def create_telemetry(tenant_id: str, device_id: str) -> dict:
    return {
        "tenant_id": tenant_id,
        "device_id": device_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature": round(random.uniform(20, 35), 2),
        "voltage": round(random.uniform(220, 240), 2),
    }


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, MQTT_PORT)
print("Device simulator started...")

while True:
    tenant_id = "tenant_001"
    device_id = f"device_{random.randint(1, 5):03d}"
    telemetry = create_telemetry(tenant_id, device_id)
    topic = f"telemetry/{device_id}/data"
    client.publish(topic, json.dumps(telemetry))
    print(f"Published: {telemetry}")
    time.sleep(2)