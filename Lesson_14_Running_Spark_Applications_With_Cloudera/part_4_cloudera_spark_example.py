spark = SparkSession.builder \
    .appName("Cloudera Spark Example") \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.instances", "4") \
    .config("spark.yarn.am.memory", "512m") \
    .getOrCreate()
