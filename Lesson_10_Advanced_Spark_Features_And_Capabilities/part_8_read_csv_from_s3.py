df = spark.read.csv("s3a://your-bucket-name/data.csv", header=True, inferSchema=True)
