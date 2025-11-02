users_df.cache()  # Caches the DataFrame in memory

# Now, any action performed on users_df will be faster
user_count = users_df.count()  # First call caches the DataFrame
