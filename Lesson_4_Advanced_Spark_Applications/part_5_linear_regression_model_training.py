from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Assembling feature vectors
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
training_data = assembler.transform(optimized_df)

# Training a linear regression model
lr = LinearRegression(featuresCol='features', labelCol='label_column')
model = lr.fit(training_data)

# Making predictions
predictions = model.transform(training_data)
predictions.select("features", "label_column", "prediction").show()
