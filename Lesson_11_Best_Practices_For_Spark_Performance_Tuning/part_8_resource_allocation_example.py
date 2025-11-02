spark = SparkSession.builder \
    .appName("Resource Allocation Example") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "4") \
    .getOrCreate()
