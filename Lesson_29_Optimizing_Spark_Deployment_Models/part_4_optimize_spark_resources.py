from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("OptimizingSpark") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
