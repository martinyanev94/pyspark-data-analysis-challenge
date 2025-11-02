from pyspark.sql import SparkSession

# Creating a Spark session
spark = SparkSession.builder \
    .appName("Advanced Spark Applications") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .getOrCreate()

# Reading a large dataset from HDFS
df = spark.read.csv("hdfs://localhost:9000/data/large_dataset.csv", header=True, inferSchema=True)
