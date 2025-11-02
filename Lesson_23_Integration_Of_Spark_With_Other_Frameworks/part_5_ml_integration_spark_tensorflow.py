from pyspark.sql import SparkSession
import pandas as pd
import tensorflow as tf

spark = SparkSession.builder \
    .appName("Machine Learning Integration Example") \
    .getOrCreate()

# Read data using Spark
spark_df = spark.read.csv("input_data.csv", header=True, inferSchema=True)

# Convert Spark DataFrame to Pandas for TensorFlow
pandas_df = spark_df.toPandas()

# Training a simple TensorFlow model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(pandas_df.shape[1]-1,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(pandas_df.drop('target', axis=1).values, pandas_df['target'].values, epochs=10)
