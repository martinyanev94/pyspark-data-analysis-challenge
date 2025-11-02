from delta import *

# Enabling Delta Lake
builder = SparkSession.builder.appName("DeltaExample").config("spark.sql.extensions", "DeltaSparkExtensions")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Writing a DataFrame in Delta format
df.write.format("delta").save("output/delta_table")

# Reading the Delta table
delta_df = spark.read.format("delta").load("output/delta_table")
