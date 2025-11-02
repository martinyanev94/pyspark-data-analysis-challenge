from pyspark.sql import functions as F

# Group data by 'category' and compute the average
averages = data.groupBy("category").agg(F.avg("value").alias("average_value"))
averages.show()
