from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Streaming Example") \
    .getOrCreate()

# Create DataFrame representing the stream of input lines from connection tohost:port
lines = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Count the number of words in each line
words = lines.select(
   explode(split(lines.value, ' ')).alias('word')
)

word_counts = words.groupBy("word").count()

# Start running the query that prints the running counts to the console
query = word_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
