from faker import Faker
import pandas as pd
import random

fake = Faker()

NUM_RECORDS = 200

categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Sports",
    "Beauty",
    "Books",
    "Toys",
    "Automotive"
]

brands = [
    "TechNova",
    "UrbanStyle",
    "HomeCraft",
    "FitGear",
    "GlowPlus",
    "ReadMore",
    "PlayTime",
    "AutoDrive",
    "PrimeEdge",
    "NextGen"
]

products = []

for i in range(1, NUM_RECORDS + 1):
    products.append({
        "product_id": f"PROD-{i}",
        "category": random.choice(categories),
        "price": round(random.uniform(5.99, 999.99), 2),
        "brand": random.choice(brands)
    })

df = pd.DataFrame(products)
df.to_csv("data/bronze/products.csv", index=False)

print(f"Generated {NUM_RECORDS} products")