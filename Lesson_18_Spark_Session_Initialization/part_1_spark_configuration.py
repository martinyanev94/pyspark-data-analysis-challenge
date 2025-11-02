spark = SparkSession.builder \
    .appName("My Spark Application") \
    .master("local[*]") \
    .getOrCreate()
spark = SparkSession.builder \
    .appName("My Spark Application") \
    .master("local[*]") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()
