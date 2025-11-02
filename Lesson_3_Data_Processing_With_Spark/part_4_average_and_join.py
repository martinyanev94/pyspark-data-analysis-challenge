from pyspark.sql.functions import avg

# Calculating the average of a column
avg_result = df_from_csv.select(avg("columnName")).collect()
print(avg_result)
# Assuming df1 and df2 are two DataFrames
joined_df = df1.join(df2, df1.id == df2.id, "inner")

# Displaying the result of the join
joined_df.show()
