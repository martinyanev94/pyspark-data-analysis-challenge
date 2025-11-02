# Caching the DataFrame
optimized_df.cache()

# Performing some transformations
result_df = optimized_df.filter(optimized_df["column_name"] > 100) \
    .select("column_name", "another_column")

result_df.show()
