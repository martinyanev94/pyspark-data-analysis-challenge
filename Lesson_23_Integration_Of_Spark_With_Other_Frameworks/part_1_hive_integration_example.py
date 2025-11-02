from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Hive Integration Example") \
    .enableHiveSupport() \
    .getOrCreate()

# Querying a Hive table
hive_df = spark.sql("SELECT * FROM hive_table")
hive_df.show()
