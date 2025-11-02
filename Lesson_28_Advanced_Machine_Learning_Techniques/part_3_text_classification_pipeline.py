from pyspark.sql import SparkSession
from pyspark.ml.feature import HashingTF, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

# Create a Spark session
spark = SparkSession.builder \
    .appName("TextClassificationExample") \
    .getOrCreate()

# Load your text data
data = spark.read.csv("text_data.csv", header=True, inferSchema=True)

# Define the hashing TF feature
hashing_tf = HashingTF(inputCol="text", outputCol="rawFeatures")
idf = IDF(inputCol="rawFeatures", outputCol="features")

# Create a logistic regression model
lr = LogisticRegression(labelCol="label")

# Create a pipeline
pipeline = Pipeline(stages=[hashing_tf, idf, lr])

# Train the model
model = pipeline.fit(data)

# Make predictions
predictions = model.transform(data)

# Evaluate the model
accuracy = predictions.filter(predictions.label == predictions.prediction).count() / float(data.count())
print(f"Accuracy: {accuracy}")
