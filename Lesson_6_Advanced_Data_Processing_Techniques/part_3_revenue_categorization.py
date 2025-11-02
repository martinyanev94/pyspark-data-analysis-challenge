from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define UDF
def categorize_revenue(revenue):
    if revenue < 100:
        return "Low"
    elif revenue < 300:
        return "Medium"
    else:
        return "High"

categorize_revenue_udf = udf(categorize_revenue, StringType())

# Apply UDF to DataFrame
df_categorized = df.withColumn("Revenue_Category", categorize_revenue_udf(df["Revenue"]))
df_categorized.show()
