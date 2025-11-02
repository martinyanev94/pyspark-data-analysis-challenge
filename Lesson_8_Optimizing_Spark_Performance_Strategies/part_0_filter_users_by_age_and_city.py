users_df = spark.read.csv("path/to/users.csv", header=True, inferSchema=True)

filtered_users = users_df.filter((users_df.age > 25) & (users_df.city == "New York"))
