transformed_df.write.mode("overwrite").parquet("path/to/save/transformed_data.parquet")
new_df = spark.read.parquet("path/to/save/transformed_data.parquet")
