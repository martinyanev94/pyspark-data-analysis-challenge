from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

# Initialize Spark Context
sc = SparkContext("local[2]", "Retail Analysis")
ssc = StreamingContext(sc, 10)

# Create a Spark session
spark = SparkSession.builder.appName("Retail Data Stream").getOrCreate()

# Create a DStream that connects to the data source
lines = ssc.socketTextStream("localhost", 9999)

# Process each line of the stream
def process_data(line):
    # Parse the data, do necessary transformations and actions
    # For example, converting line of text to data frame
    data = line.split(",")
    df = spark.createDataFrame([(data[0], data[1], data[2])], ["product_id", "timestamp", "amount"])
    # Here you can store or analyze the DataFrame

lines.foreachRDD(lambda rdd: process_data(rdd.collect()))

# Start the computation
ssc.start()
ssc.awaitTermination()
