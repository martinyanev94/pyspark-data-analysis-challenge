from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Create a Spark session
spark = SparkSession.builder \
    .appName("RandomForestExample") \
    .getOrCreate()

# Load dataset
data = spark.read.csv("data.csv", header=True, inferSchema=True)

# Feature engineering: Combine feature columns into a vector
feature_columns = ['feature1', 'feature2', 'feature3']
assembler = VectorAssembler(inputCols=feature_columns, outputCol='features')
data = assembler.transform(data)

# Split data into training and test sets
train_data, test_data = data.randomSplit([0.7, 0.3])

# Initialize Random Forest Classifier
rf = RandomForestClassifier(labelCol="label", featuresCol="features")

# Train the model
rf_model = rf.fit(train_data)

# Make predictions
predictions = rf_model.transform(test_data)

# Evaluate the model
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy: {accuracy}")
