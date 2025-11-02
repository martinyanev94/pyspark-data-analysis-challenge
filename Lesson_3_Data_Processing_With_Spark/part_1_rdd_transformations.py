# Doubling each element in the RDD
doubled_rdd = rdd.map(lambda x: x * 2)

# Collecting and printing the result
doubled_result = doubled_rdd.collect()
print(doubled_result)
# Filtering even numbers from the RDD
even_rdd = rdd.filter(lambda x: x % 2 == 0)

# Collecting and printing the result
even_result = even_rdd.collect()
print(even_result)
