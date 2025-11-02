import pandas as pd
import matplotlib.pyplot as plt

pdf = log_df.toPandas()
pdf['status'].value_counts().plot(kind='bar')
plt.title('HTTP Status Code Counts')
plt.ylabel('Frequency')
plt.show()
