output_s3_path = "s3://your-bucket-name/path/to/output/data.parquet"
df_mysql.write.mode("overwrite").parquet(output_s3_path)
