spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.yarn.executor.memoryOverhead", "512m") \
    .getOrCreate()
