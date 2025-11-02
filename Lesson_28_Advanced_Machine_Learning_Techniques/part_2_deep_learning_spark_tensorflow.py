import tensorflow as tf
from pyspark.sql import SparkSession
from pyspark import SparkFiles

# Create a Spark session
spark = SparkSession.builder \
    .appName("DeepLearningExample") \
    .getOrCreate()

# Load your data, must be in NumPy format for TensorFlow
# Here assuming you have the data saved in NumPy arrays
# e.g. X_train, y_train = np.load('data.npy'), np.load('labels.npy')

# Define a simple CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Save model
model.save("my_model.h5")

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy}')
