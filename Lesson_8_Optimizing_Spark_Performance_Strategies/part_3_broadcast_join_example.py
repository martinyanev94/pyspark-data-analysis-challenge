from pyspark.sql import functions as F

large_df = spark.read.csv("path/to/large_data.csv", header=True)
small_df = spark.read.csv("path/to/small_data.csv", header=True)

# Using broadcast to minimize shuffle
result_df = large_df.join(F.broadcast(small_df), "key_column")
