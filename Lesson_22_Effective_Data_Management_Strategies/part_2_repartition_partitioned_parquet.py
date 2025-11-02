# Assume 'df' has been created as shown earlier

# Repartitioning with a specific column
partitioned_df = df.repartition("ID")
partitioned_df.write.parquet("output/partitioned_parquet_data.parquet")
