from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

# Assuming 'data' is a DataFrame containing features and labels
vectorAssembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")

data_transformed = vectorAssembler.transform(data)

# Split the data into training and test sets
train_data, test_data = data_transformed.randomSplit([0.7, 0.3])

# Create a Linear Regression model
lr = LinearRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_data)

# Make predictions
predictions = model.transform(test_data)
predictions.select("features", "label", "prediction").show()
