coalesced_df = users_df.coalesce(10)  # Reduce to 10 partitions
repartitioned_df = users_df.repartition(20)  # Increase to 20 partitions for better distribution
