# Adjusting Spark configurations
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ConfigExample") \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()
