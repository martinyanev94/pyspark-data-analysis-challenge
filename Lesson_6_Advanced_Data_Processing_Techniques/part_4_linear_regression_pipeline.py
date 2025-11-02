from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Sample data for linear regression
data_for_lr = [(1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0), (5, 5.0)]
lr_columns = ["Features", "Label"]
df_lr = spark.createDataFrame(data_for_lr, schema=lr_columns)

# Prepare feature vector
vector_assembler = VectorAssembler(inputCols=["Features"], outputCol="features")
df_lr_vector = vector_assembler.transform(df_lr)

# Fit linear regression model
lr = LinearRegression(featuresCol="features", labelCol="Label")
model = lr.fit(df_lr_vector)

# Print out the coefficients
print(f"Coefficients: {model.coefficients}, Intercept: {model.intercept}")
