from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder \
    .appName("Kafka Integration Example") \
    .getOrCreate()

# Create a streaming DataFrame that connects to Kafka
kafkaStreamDF = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic_name") \
    .load()

# Processing the stream
processedStreamDF = kafkaStreamDF.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
