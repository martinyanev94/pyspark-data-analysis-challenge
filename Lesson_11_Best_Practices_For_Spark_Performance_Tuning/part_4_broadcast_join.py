# Assuming df1 is large and df2 is small
from pyspark.sql import functions as F

# Broadcasting the smaller DataFrame
df2_broadcast = spark.sparkContext.broadcast(df2.collect())

# Performing join with a broadcasted DataFrame
result = df1.join(F.broadcast(df2), "key")
