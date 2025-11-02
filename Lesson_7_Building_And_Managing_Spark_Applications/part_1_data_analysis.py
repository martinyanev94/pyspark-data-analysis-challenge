# Load data from a CSV file
data_frame = spark.read.csv("path/to/your/data.csv", header=True, inferSchema=True)

# Show the first few rows of the DataFrame
data_frame.show()

# Perform a transformation
transformed_df = data_frame.select("column1", "column2").filter(data_frame["column3"] > 100)

# Perform an action
result_count = transformed_df.count()
print(f"Number of records where column3 > 100: {result_count}")
