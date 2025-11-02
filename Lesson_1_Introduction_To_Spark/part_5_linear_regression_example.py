from pyspark.ml.regression import LinearRegression

# Sample data, for instance, representing independent variable 'x' and dependent variable 'y'
data = [(1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0), (5, 5.0)]
columns = ["x", "y"]

training = spark.createDataFrame(data, columns)

# Create a Linear Regression model
lr = LinearRegression(featuresCol='x', labelCol='y')

# Fit the model
lr_model = lr.fit(training)

# Print the coefficients
print(f"Coefficients: {lr_model.coefficients}, Intercept: {lr_model.intercept}")
