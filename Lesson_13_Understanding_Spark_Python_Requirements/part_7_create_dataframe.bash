jupyter notebook
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Value"]

df = spark.createDataFrame(data, columns)
df.show()
