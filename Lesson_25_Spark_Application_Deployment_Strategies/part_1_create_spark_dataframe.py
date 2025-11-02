from pyspark.sql import SparkSession

# Create a Spark session in local mode
spark = SparkSession.builder \
    .appName("LocalApp") \
    .master("local[*]") \
    .getOrCreate()

# Example: Create a DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["Name", "Id"])

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
