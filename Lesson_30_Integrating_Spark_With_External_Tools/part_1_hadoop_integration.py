from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HadoopIntegration") \
    .getOrCreate()

# Read data from HDFS
df = spark.read.csv("hdfs://<namenode-ip>:<port>/path/to/your/data.csv", header=True, inferSchema=True)
