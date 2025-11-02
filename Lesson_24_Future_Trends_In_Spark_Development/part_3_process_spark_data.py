from pyspark.sql import SparkSession

def process_data(event, context):
    spark = SparkSession.builder \
        .appName("Serverless Spark Job") \
        .getOrCreate()

    # Read data triggered by event
    data_path = event['dataPath']
    df = spark.read.csv(data_path, header=True, inferSchema=True)

    # Process data
    processed_df = df.groupBy("some_column").count()
    processed_df.write.csv("s3://your-bucket-name/processed_data.csv")
