from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySparkApplication") \
    .config("spark.some.config.option", "config-value") \
    .getOrCreate()
