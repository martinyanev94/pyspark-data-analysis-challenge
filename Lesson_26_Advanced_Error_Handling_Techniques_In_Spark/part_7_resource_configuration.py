from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ResourceConfiguration") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "1g") \
    .getOrCreate()

# Your Spark application logic here
