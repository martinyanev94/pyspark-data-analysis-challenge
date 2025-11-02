df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)
df.show()
