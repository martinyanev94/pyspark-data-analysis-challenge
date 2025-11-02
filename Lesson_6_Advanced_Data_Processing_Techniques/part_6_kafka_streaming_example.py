from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaStreamingExample") \
    .getOrCreate()

# Define Kafka source
kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "my-topic") \
    .load()

# Process the stream
query = kafka_stream.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
