from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Hadoop Integration Example") \
    .getOrCreate()

# Reading a CSV file from HDFS
df = spark.read.csv("hdfs://localhost:9000/user/data/input.csv", header=True, inferSchema=True)
df.show()
