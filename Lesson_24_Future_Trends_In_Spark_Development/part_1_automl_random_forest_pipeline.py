from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline

spark = SparkSession.builder \
    .appName("AutoML Example") \
    .getOrCreate()

# Sample data
data = spark.createDataFrame([
    (0, 1.0, 0.1, 0.2),
    (1, 0.0, 0.2, 0.1),
    (2, 1.0, 0.3, 0.4),
    (3, 0.0, 0.4, 0.3)
], ["id", "label", "feature1", "feature2"])

# Feature engineering
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")

# Model training
classifier = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)

# Create a pipeline
pipeline = Pipeline(stages=[assembler, classifier])

# Fit the model
model = pipeline.fit(data)
