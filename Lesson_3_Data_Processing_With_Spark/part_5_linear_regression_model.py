from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Assembling feature vectors
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
training_data = assembler.transform(df_from_csv)

# Training a linear regression model
lr = LinearRegression(featuresCol='features', labelCol='label')
model = lr.fit(training_data)

# Making predictions 
predictions = model.transform(training_data)
predictions.show()
