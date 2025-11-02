from pyspark.sql import SparkSession

def run_edge_spark_job():
    spark = SparkSession.builder \
        .appName("Edge Computing with Spark") \
        .getOrCreate()

    # Simulated edge data stream
    edge_df = spark.readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 9999) \
        .load()

    # Process the data stream
    processed_stream = edge_df.groupBy("sensor_id").avg("value")

    query = processed_stream.writeStream \
        .outputMode("update") \
        .format("console") \
        .start()

    query.awaitTermination()
