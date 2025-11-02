spark = SparkSession.builder \
    .appName("GarbageCollectionOptimizedSparkApplication") \
    .config("spark.executor.extraJavaOptions", "-XX:+UseG1GC") \
    .config("spark.driver.extraJavaOptions", "-XX:+UseG1GC") \
    .getOrCreate()
