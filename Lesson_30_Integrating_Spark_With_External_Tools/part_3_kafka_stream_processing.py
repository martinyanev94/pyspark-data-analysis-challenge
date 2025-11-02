from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("KafkaIntegration") \
    .getOrCreate()

# Read data stream from Kafka
kafkaStream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "<kafka-server-ip>:<port>") \
    .option("subscribe", "<your_topic>") \
    .load()

# Define the transformation logic
transformed = kafkaStream.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Output the streaming DataFrame to console
query = transformed.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
