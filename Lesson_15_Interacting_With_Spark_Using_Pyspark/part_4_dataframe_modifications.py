from pyspark.sql.functions import when

# Adding a new column for senior citizens
df_with_senior_flag = df.withColumn("is_senior", when(df["age"] >= 65, True).otherwise(False))
df_with_senior_flag.show()
# Increasing salary by 10%
df_with_salary_increase = df.withColumn("salary", df["salary"] * 1.10)
df_with_salary_increase.show()
