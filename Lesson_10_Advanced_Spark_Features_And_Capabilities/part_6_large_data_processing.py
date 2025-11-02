data = spark.read.csv("path/to/large_data.csv", header=True, inferSchema=True).repartition(10)
