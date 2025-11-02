import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SparkApplication")

logger.info("Starting Spark Application")

try:
    # Spark application logic here
    data_frame = spark.read.csv("path/to/your/data.csv", header=True, inferSchema=True)
    logger.info("Data successfully loaded")
except Exception as e:
    logger.error("An error occurred: %s", e)
