status_counts = log_df.groupBy('status').count()
status_counts.show()
