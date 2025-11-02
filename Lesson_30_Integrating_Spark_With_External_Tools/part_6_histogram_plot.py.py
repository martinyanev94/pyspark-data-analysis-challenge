import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your Spark DataFrame
pandas_df = df.toPandas()

# Create a histogram of a specific column
pandas_df['column_name'].hist(bins=20)
plt.title('Histogram of Column Name')
plt.xlabel('Column Values')
plt.ylabel('Frequency')
plt.show()
