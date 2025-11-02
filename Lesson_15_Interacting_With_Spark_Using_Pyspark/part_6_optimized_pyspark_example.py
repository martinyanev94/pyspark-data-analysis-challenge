spark = SparkSession.builder \
    .appName("Optimized PySpark Example") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
# Repartitioning the DataFrame into 8 partitions
repartitioned_df = df.repartition(8)
# Coalescing to 2 partitions
coalesced_df = df.coalesce(2)
