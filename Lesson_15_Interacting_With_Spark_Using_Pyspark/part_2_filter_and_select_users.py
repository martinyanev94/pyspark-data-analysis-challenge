# Filtering users from a specific country
filtered_df = df.filter(df['country'] == 'USA')
filtered_df.show()
# Selecting specific columns
selected_df = df.select("name", "age", "country")
selected_df.show()
