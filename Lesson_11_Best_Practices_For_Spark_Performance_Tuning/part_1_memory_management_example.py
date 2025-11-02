from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Memory Management Example") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
