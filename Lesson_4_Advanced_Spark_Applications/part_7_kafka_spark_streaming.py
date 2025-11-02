# Setting up the Spark session with Kafka
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Reading streaming data from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic_name") \
    .load()

# Displaying the streaming DataFrame
kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()
