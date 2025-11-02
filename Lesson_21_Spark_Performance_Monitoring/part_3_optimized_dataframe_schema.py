# Use DataFrame's built-in types
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
])

data = spark.read.schema(schema).csv("optimized_dataset.csv")
