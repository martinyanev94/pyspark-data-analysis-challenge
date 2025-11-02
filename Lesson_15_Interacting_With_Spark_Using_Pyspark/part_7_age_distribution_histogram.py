import pandas as pd
import matplotlib.pyplot as plt

# Convert PySpark DataFrame to Pandas
pandas_df = df.toPandas()

# Plotting
pandas_df['age'].hist(bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
