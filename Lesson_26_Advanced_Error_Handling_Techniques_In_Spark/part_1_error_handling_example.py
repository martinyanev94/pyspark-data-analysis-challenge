from pyspark import SparkContext

sc = SparkContext(appName="ErrorHandlingExample")

# Creating an RDD
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# A transformation that will cause an error during execution
transformation = rdd.map(lambda x: 10 / (x - 3))

# The error will not be triggered here; it happens during the action
result = transformation.collect()
print(result)
