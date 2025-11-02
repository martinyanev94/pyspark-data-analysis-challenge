from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Introduction to Spark") \
    .getOrCreate()
