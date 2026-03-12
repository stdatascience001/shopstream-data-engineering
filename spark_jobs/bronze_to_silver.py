from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, upper, trim, when, isnan

spark = SparkSession.builder.appName('BronzeToSilver').getOrCreate()

# Read raw CSV from bronze layer
df = spark.read.csv('data/bronze/orders_*.csv', header=True, inferSchema=True)

# Clean: drop nulls in critical columns
df = df.dropna(subset=['order_id', 'customer_id', 'amount'])

# Clean: remove duplicate order IDs
df = df.dropDuplicates(['order_id'])

# Cast and standardize
df = df.withColumn('order_date', to_date(col('order_date')))
df = df.withColumn('status', upper(trim(col('status'))))
df = df.filter(col('amount') > 0)

# Write to silver as Parquet (partitioned by date)
df.write.mode('overwrite').partitionBy('order_date') \
    .parquet('data/silver/orders/')

print(f'Silver layer written: {df.count()} clean records')
spark.stop()