# Read data with specified number of partitions
data = spark.read.csv("path/to/huge_data.csv", header=True, inferSchema=True).repartition(10)
