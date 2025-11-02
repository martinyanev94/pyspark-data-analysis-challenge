df_mysql_partitioned = spark.read.jdbc(
    url=jdbc_url,
    table="your_table",
    properties=properties,
    numPartitions=10,
    partitionColumn="id",
    lowerBound=1,
    upperBound=10000
)
