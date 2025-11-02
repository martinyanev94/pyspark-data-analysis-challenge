# Assuming 'df' is our DataFrame loaded earlier
df_filtered = df.filter(df.age > 21)

# Select specific columns
df_selected = df_filtered.select("name", "age")
df_selected.show()
