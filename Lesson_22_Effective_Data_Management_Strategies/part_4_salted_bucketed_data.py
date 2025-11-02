import pyspark.sql.functions as F

# Adding a salt to the 'ID' column to handle data skew
salted_df = df.withColumn("salt", F.round(F.rand() * 4)) \
               .withColumn("salted_ID", F.concat(df["ID"], F.lit("_"), df["salt"]))
salted_df.show()
# Writing the DataFrame to disk as bucketed data
df.write \
    .bucketBy(4, "ID") \
    .saveAsTable("bucketed_table")
