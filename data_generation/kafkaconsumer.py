from kafka import KafkaConsumer
import json, os
from datetime import datetime

consumer = KafkaConsumer("clickstream",
    bootstrap_servers = "localhost:9092",
    value_deserializer = lambda m: json.loads(m.decode()),
    auto_offset_reset = "earliest",
    group_id="shopstream-consumer")

buffer = []
for msg in consumer:
    buffer.append(msg.value)
    if len(buffer) >= 1000:
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        path = f"data/bronze/clicks_{ts}.json"
        with open(path, 'w') as f:
            json.dump(buffer, f)
        buffer = []
        print(f'Wrote batch to {path}')