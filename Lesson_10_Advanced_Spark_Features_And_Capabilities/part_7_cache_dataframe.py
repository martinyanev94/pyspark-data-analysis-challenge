# Caching the DataFrame
df.cache()

# Perform some actions to trigger caching
df.count()

# Now the next action will make use of the cached DataFrame
df.show()
