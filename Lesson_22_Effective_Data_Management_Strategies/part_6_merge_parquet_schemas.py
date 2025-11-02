# Merging schemas when reading Parquet files
updated_df = spark.read.option("mergeSchema", "true").parquet("output/partitioned_parquet_data.parquet")
