# Spark batch processing
spark_df = spark.read.csv("input_data.csv")
spark_df.write.parquet("processed_data.parquet")

# Flink job to consume processed data and apply real-time analytics
# Flink code would go here to read from Kafka or adapt the parquet output
