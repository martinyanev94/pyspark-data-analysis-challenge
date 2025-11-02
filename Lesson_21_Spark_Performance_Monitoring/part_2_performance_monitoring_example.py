from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Performance Monitoring Example") \
    .getOrCreate()

# Load a large dataset
data = spark.read.csv("large_dataset.csv", header=True, inferSchema=True)

# Perform some transformations
transformed_data = data.groupBy("column_name").agg({"other_column": "sum"})

# Action that triggers the execution
result = transformed_data.collect()
