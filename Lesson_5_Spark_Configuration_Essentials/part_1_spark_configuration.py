from pyspark import SparkConf, SparkContext

# Create a SparkConf object
conf = SparkConf()
conf.setAppName("MySparkApp")\
    .setMaster("local[2]")\
    .set("spark.executor.memory", "4g")\
    .set("spark.executor.cores", "2")

# Initialize SparkContext with this configuration
sc = SparkContext(conf=conf)

print("SparkConf settings:")
print(conf.getAll())
