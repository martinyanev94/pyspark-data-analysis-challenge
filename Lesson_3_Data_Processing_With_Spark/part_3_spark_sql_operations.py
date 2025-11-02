# Registering DataFrame as a temporary view
df.createOrReplaceTempView("numbers")

# Running a simple SQL query
sql_result = spark.sql("SELECT * FROM numbers WHERE value > 2")
sql_result.show()
# Reading data from a CSV file stored in HDFS
df_from_csv = spark.read.csv("hdfs://your-hadoop-cluster/data/sample.csv", header=True, inferSchema=True)

# Displaying the DataFrame
df_from_csv.show()
