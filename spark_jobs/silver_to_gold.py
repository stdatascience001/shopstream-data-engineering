from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg, countDistinct

spark = SparkSession.builder.appName('SilverToGold').getOrCreate()

orders = spark.read.parquet('data/silver/orders/')

# Daily Revenue Summary
daily_revenue = orders.groupBy('order_date') \
    .agg(
        sum('amount').alias('total_revenue'),
        count('order_id').alias('total_orders'),
        countDistinct('customer_id').alias('unique_customers'),
        avg('amount').alias('avg_order_value')
    ).orderBy('order_date')

daily_revenue.write.mode('overwrite') \
    .parquet('data/gold/daily_revenue/')

print('Gold layer written successfully')
spark.stop()