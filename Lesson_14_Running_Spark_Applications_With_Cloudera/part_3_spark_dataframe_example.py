from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Cloudera Spark Example") \
    .getOrCreate()

# Create a DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Value"]

df = spark.createDataFrame(data, columns)

# Show the DataFrame content
df.show()

# Perform a transformation: Add a new column
df_with_new_column = df.withColumn("NewValue", df["Value"] * 2)
df_with_new_column.show()
