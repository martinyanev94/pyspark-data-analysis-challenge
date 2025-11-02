from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

# Create Spark session
spark = SparkSession.builder \
    .appName("Fraud Detection") \
    .getOrCreate()

# Load the training data
data = spark.read.csv("path/to/transaction_data.csv", header=True)

# Feature engineering
feature_columns = ['amount', 'location', 'transaction_time']
vector_assembler = VectorAssembler(inputCols=feature_columns, outputCol='features')
data_transformed = vector_assembler.transform(data)

# Train the model
lr = LogisticRegression(featuresCol='features', labelCol='label')
model = lr.fit(data_transformed)

# Make predictions
predictions = model.transform(data_transformed)
predictions.select('amount', 'prediction').show()
