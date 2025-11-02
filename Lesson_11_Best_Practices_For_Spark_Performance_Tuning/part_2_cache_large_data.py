# Load some data
data = spark.read.csv("path/to/large_data.csv", header=True, inferSchema=True)

# Cache the DataFrame in memory
data.cache()

# Trigger an action to materialize the cache
data.count()  # This will cache the data in memory
