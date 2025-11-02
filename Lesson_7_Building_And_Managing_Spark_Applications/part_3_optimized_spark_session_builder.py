spark = SparkSession.builder \
    .appName("OptimizedSparkApplication") \
    .config("spark.executor.cores", "4") \
    .config("spark.executor.memory", "8g") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()
