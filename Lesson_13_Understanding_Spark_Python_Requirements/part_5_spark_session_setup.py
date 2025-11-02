from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("My Spark Application") \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()
