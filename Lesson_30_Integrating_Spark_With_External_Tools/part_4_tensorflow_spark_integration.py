import tensorflow as tf
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TensorFlowIntegration") \
    .getOrCreate()

# Load your data into a DataFrame
df = spark.read.csv("path/to/your/data.csv", header=True, inferSchema=True)

# Convert DataFrame to a TensorFlow dataset
train_data = df.toPandas()
train_dataset = tf.data.Dataset.from_tensor_slices((train_data['features'], train_data['labels']))
train_dataset = train_dataset.batch(32)

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(train_data['features'].shape[1],)),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_dataset, epochs=10)
