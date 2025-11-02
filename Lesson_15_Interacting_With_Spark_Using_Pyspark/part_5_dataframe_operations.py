# Performing an inner join
joined_df = df1.join(df2, on="user_id", how="inner")
joined_df.show()
# Removing duplicate entries
distinct_df = df.dropDuplicates(["user_id"])
distinct_df.show()
