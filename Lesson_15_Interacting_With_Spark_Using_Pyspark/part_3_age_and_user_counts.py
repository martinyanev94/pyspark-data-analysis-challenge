# Calculating the average age
average_age = df.groupBy("country").agg({"age": "avg"})
average_age.show()
# Counting users per country
user_counts = df.groupBy("country").count()
user_counts.show()
