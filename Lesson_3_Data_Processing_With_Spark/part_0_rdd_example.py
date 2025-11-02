from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RDD Example") \
    .getOrCreate()

data = [1, 2, 3, 4, 5]

# Creating an RDD from a list
rdd = spark.sparkContext.parallelize(data)

# Collecting the RDD to see the result
result = rdd.collect()
print(result)
