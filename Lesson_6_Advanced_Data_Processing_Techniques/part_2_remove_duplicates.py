# Sample data with duplicates
data_with_duplicates = [("Product A", 10, 200),
                        ("Product B", 5, 100),
                        ("Product A", 10, 200),
                        ("Product C", 6, 120)]
df_with_duplicates = spark.createDataFrame(data_with_duplicates, schema=columns)

# Removing duplicates
df_deduplicated = df_with_duplicates.dropDuplicates()
df_deduplicated.show()
