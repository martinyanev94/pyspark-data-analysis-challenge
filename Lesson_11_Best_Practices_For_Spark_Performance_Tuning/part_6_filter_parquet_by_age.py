# Load a parquet file with filtering
filtered_data = spark.read.parquet("path/to/data.parquet").filter("age > 21")
filtered_data.show()
