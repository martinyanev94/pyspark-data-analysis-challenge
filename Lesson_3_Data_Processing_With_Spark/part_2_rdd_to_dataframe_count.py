# Counting the number of elements in the RDD
count_result = rdd.count()
print(count_result)
from pyspark.sql import Row

# Creating an RDD of rows
row_rdd = rdd.map(lambda x: Row(value=x))

# Converting RDD to DataFrame
df = spark.createDataFrame(row_rdd)

# Displaying the DataFrame
df.show()
