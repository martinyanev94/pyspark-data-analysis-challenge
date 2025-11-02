# Registering the DataFrame as a temporary view
optimized_df.createOrReplaceTempView("optimized_table")

# Executing an SQL query
sql_result = spark.sql("SELECT column_name, AVG(another_column) AS avg_value FROM optimized_table GROUP BY column_name")
sql_result.show()
