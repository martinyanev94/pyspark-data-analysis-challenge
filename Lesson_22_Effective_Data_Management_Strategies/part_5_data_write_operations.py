# Overwriting previous data
df.write.mode("overwrite").parquet("output/overwrite_data.parquet")
# Appending new data
new_data.show()
new_data.write.mode("append").parquet("output/append_data.parquet")
