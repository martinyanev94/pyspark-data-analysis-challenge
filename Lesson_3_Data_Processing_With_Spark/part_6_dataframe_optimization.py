# Repartitioning the DataFrame for better performance
optimized_df = df_from_csv.repartition(4)

# Displaying the number of partitions
print(optimized_df.rdd.getNumPartitions())
# Caching the DataFrame
df_from_csv.cache()
