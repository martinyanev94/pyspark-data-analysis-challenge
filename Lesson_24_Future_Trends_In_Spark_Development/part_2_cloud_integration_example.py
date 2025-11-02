spark = SparkSession.builder \
    .appName("Cloud Integration Example") \
    .getOrCreate()

# Reading data from S3
s3_df = spark.read.csv("s3://your-bucket-name/input_data.csv", header=True, inferSchema=True)
s3_df.show()

# Basic transformation
results = s3_df.groupBy("some_column").count()
results.show()
