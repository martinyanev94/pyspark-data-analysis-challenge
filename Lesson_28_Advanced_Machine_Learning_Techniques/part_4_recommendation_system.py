from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Create a Spark session
spark = SparkSession.builder \
    .appName("RecommendationSystemExample") \
    .getOrCreate()

# Load your interactions data
data = spark.read.csv("interactions.csv", header=True, inferSchema=True)

# Define the ALS model
als = ALS(maxIter=10, regParam=0.01, userCol="userId", itemCol="itemId", ratingCol="rating", coldStartStrategy="drop", nonnegative=True)

# Train the model
model = als.fit(data)

# Generate predictions
predictions = model.transform(data)

# Evaluate the model
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print(f"RMSE: {rmse}")
