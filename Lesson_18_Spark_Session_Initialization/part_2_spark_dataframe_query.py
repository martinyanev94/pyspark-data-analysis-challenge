for key, value in spark.sparkContext.getConf().getAll():
    print(f"{key}: {value}")
# Sample DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Id"]

df = spark.createDataFrame(data, columns)
df.createOrReplaceTempView("people")

# Running SQL query
result = spark.sql("SELECT * FROM people WHERE Id > 1")
result.show()
