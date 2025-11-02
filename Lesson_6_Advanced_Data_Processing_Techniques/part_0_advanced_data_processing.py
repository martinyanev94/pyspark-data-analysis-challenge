from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("AdvancedDataProcessing").getOrCreate()

# Sample data
data = [("Product A", 10, 200),
        ("Product B", 5, 100),
        ("Product A", 4, 80),
        ("Product C", 6, 120)]
columns = ["Product", "Quantity", "Revenue"]

# Creating DataFrame
df = spark.createDataFrame(data, schema=columns)

# Aggregating revenue per product
total_revenue = df.groupBy("Product").agg(sum("Revenue").alias("Total_Revenue"))
total_revenue.show()
