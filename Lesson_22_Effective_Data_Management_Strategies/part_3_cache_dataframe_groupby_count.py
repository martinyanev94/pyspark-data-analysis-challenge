# Caching the DataFrame for future use
df.cache()

# Performing actions on the cached DataFrame
result = df.groupBy("Name").count().collect()
print(result)
