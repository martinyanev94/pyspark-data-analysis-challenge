from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Interaction Example") \
    .getOrCreate()
