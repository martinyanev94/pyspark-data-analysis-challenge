from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("Spark SQL Example") \
    .getOrCreate()

# Load data into a DataFrame from a JSON file
df = spark.read.json("path/to/people.json")

# Create a temporary view to run SQL queries
df.createOrReplaceTempView("people")

# Execute SQL query
result = spark.sql("SELECT name, age FROM people WHERE age > 21")
result.show()
