spark = SparkSession.builder \
    .appName("My Spark Application") \
    .config("spark.executor.cores", "4") \
    .getOrCreate()
