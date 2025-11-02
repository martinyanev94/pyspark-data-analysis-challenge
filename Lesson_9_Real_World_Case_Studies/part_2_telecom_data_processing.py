from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Telecom Data Processing") \
    .getOrCreate()

# Load data into a DataFrame
df_calls = spark.read.csv("path/to/calls_data.csv", header=True)

# Execute SQL queries directly against DataFrame
df_calls.createOrReplaceTempView("calls")

# Example: Getting count of calls by customer ID
customer_call_counts = spark.sql("SELECT customer_id, COUNT(*) as call_count FROM calls GROUP BY customer_id")

# Show the result
customer_call_counts.show()
