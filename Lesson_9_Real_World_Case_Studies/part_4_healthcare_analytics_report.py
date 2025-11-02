from pyspark.sql import SparkSession

# Set up Spark session
spark = SparkSession.builder.appName("Healthcare Analytics").getOrCreate()

# Load patient data
patient_data = spark.read.json("path/to/patient_data.json")

# Transform and analyze
report = patient_data.groupBy('condition').agg({'treatment_cost': 'avg', 'patient_id': 'count'})

# Display the healthcare report
report.show()
