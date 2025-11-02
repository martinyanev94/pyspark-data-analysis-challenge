# Writing data to Parquet format
users_df.write.mode("overwrite").parquet("path/to/users_parquet.parquet")

# Reading back the Parquet file
new_users_df = spark.read.parquet("path/to/users_parquet.parquet")
