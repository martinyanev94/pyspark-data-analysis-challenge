from pyspark.mllib import ClassificationModel
from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.linalg import Vectors

# Initialize the Spark Context
sc = SparkContext("local", "Logistic Regression Example")

# Example data: label and features
data = [
    (0.0, Vectors.dense([0.0, 1.0])),
    (1.0, Vectors.dense([1.0, 0.0])),
    (0.0, Vectors.dense([1.0, 1.0])),
    (1.0, Vectors.dense([0.0, 0.0])),
]

# Parallelize the data
training_data = sc.parallelize(data)

# Train the Logistic Regression model
model = LogisticRegressionWithSGD.train(training_data)

# Make predictions
prediction = model.predict(Vectors.dense([0.0, 1.0]))
print("Prediction for [0.0, 1.0]:", prediction)
