from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

def visualize_data():
    spark = SparkSession.builder \
        .appName("Visualization Example") \
        .getOrCreate()

    # Read data and run analysis
    data_df = spark.read.csv("s3://your-bucket-name/input_data.csv", header=True, inferSchema=True)
    summary = data_df.groupBy("category").count().toPandas()

    # Create a bar plot
    plt.bar(summary['category'], summary['count'])
    plt.title('Data Summary by Category')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

visualize_data()
