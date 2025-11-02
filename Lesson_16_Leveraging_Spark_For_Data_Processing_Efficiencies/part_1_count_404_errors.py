not_found_rdd = log_rdd.filter(lambda line: '404' in line)
count_404s = not_found_rdd.count()
print(f"Number of 404 errors: {count_404s}")
