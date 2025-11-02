from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HiveIntegration") \
    .enableHiveSupport() \
    .getOrCreate()

# Query Hive table
df = spark.sql("SELECT * FROM your_hive_table WHERE some_column > some_value")
