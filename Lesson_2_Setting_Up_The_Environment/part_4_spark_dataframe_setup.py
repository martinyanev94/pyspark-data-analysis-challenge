from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Test Spark Setup") \
    .getOrCreate()

print(spark.version)
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Id"]

df = spark.createDataFrame(data, columns)
df.show()
