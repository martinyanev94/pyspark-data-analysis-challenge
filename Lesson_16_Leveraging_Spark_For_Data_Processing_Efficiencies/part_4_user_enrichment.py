user_lookup = {"1": "Alice", "2": "Bob", "3": "Charlie"}
broadcast_user_lookup = spark.sparkContext.broadcast(user_lookup)
enriched_logs_rdd = log_rdd.map(lambda line: (line, broadcast_user_lookup.value.get(line.split()[0], "Unknown")))
