from faker import Faker
import pandas as pd, random, uuid

fake = Faker()
NUM_RECORDS = 50000

customers = []
for _ in range(NUM_RECORDS):
    customers.append({
        "customer_id" : str(uuid.uuid4()),
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "country": fake.country(),
        "signup_date": fake.date_between("-3y", "today").isoformat()
    })

df = pd.DataFrame(customers)
df.to_csv("data/bronze/customers.csv", index=False)
print(f"Generated {NUM_RECORDS} customers")