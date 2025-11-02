spark = SparkSession.builder \
    .appName("My Spark Application") \
    .config("spark.sql.shuffle.partitions", "50") \
    .getOrCreate()
df = spark.read.csv("path/to/data.csv", header=True, inferSchema=True)
df.cache()
