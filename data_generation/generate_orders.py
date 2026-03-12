from faker import Faker
import pandas as pd, random, uuid

fake = Faker()
NUM_RECORDS = 50000

orders = []
for _ in range(NUM_RECORDS):
    orders.append({
        "order_id": str(uuid.uuid4()),
        "customer_id": str(uuid.uuid4()),
        "product_id": f"PROD-{random.randint(1,200)}",
        "quantity": random.randint(1,5),
        "amount": round(random.uniform(5.99, 499.99), 2),
        "order_date": fake.date_between("-2y", "today").isoformat(),
        "status": random.choice(["completed","pending","refunded","shipped"])
    })

df = pd.DataFrame(orders)
df.to_csv("data/bronze/orders.csv", index=False)
print(f"Generated {NUM_RECORDS} orders")