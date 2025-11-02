spark = SparkSession.builder \
    .appName("AWS S3 Integration Example") \
    .getOrCreate()

# Reading a file from S3
s3_df = spark.read.csv("s3://your-bucket-name/input_data.csv", header=True, inferSchema=True)
s3_df.show()
