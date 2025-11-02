from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Housing Price Prediction") \
    .getOrCreate()

# Sample data
data = spark.createDataFrame([
    (1, 3000, 400000),
    (2, 2500, 340000),
    (3, 1500, 200000),
    (4, 2300, 290000),
], ["id", "size", "price"])

# Prepare features
assembler = VectorAssembler(inputCols=["size"], outputCol="features")
training_data = assembler.transform(data)

# Create a linear regression model
lr = LinearRegression(featuresCol='features', labelCol='price')
model = lr.fit(training_data)

# Display the coefficients and intercept
print(f"Coefficients: {model.coefficients}, Intercept: {model.intercept}")
