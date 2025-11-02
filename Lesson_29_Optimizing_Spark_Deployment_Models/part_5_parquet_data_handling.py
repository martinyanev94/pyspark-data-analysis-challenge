df.write.parquet("output_data.parquet")
df = spark.read.parquet("output_data.parquet")
