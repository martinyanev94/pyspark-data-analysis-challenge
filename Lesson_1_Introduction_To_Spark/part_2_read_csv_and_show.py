df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()
