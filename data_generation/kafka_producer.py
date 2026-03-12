from kafka import KafkaProducer
import json, time, random, uuid
from faker import Faker

fake = Faker()
producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=lambda v: json.dumps(v).encode("utf-8"))

while True:
    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": str(uuid.uuid4()),
        "page": random.choice(["/home","/product","/cart","/checkout"]),
        "action": random.choice(["view","click","add_to_cart","purchase"]),
        "timestamp": fake.iso8601()
    }
    producer.send("clickstream", value=event)
    time.sleep(0.5) # send 2 events per second