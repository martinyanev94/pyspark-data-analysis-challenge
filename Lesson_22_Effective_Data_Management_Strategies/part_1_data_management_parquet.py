from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Data Management Example") \
    .getOrCreate()

# Creating a sample DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "ID"]
df = spark.createDataFrame(data, columns)

# Writing the DataFrame to a Parquet file
df.write.parquet("output/parquet_data.parquet")

# Reading the Parquet file back into a DataFrame
parquet_df = spark.read.parquet("output/parquet_data.parquet")
parquet_df.show()
