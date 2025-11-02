from pyspark.sql import Row

# Create a list of Rows with structured data
rows = log_rdd.map(lambda line: Row(status=line.split()[8], url=line.split()[6]))

# Convert to DataFrame and define the schema
log_df = spark.createDataFrame(rows)

log_df.show()
