from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("MySparkSQLApp") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.sql.caseSensitive", "true") \
    .getOrCreate()

print("Spark SQL settings:")
print(spark.conf.getAll())
