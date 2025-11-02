from pyspark.sql import Window
from pyspark.sql.functions import sum as sum_

# Define window specification
windowSpec = Window.partitionBy("Product").orderBy("Revenue")

# Calculate running total
df_with_running_total = df.withColumn("Running_Total", sum_("Revenue").over(windowSpec))
df_with_running_total.show()
