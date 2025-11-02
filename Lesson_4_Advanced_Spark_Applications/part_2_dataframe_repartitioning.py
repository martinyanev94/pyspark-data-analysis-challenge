# Repartitioning the DataFrame to improve performance
optimized_df = df.repartition(8)  # Increasing the number of partitions to 8

# Displaying the number of partitions
print(f"Number of partitions: {optimized_df.rdd.getNumPartitions()}")
