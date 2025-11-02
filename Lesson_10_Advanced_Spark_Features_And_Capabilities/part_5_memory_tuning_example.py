from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Memory Tuning Example") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()
