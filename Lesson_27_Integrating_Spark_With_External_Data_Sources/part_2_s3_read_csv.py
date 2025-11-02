from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("S3ReadExample") \
    .getOrCreate()

s3_path = "s3://your-bucket-name/path/to/s3/file.csv"
df = spark.read.csv(s3_path, header=True, inferSchema=True)
df.show()
