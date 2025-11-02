import logging
from pyspark import SparkContext

# Setting up the logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def process_with_logging(x):
    try:
        return 10 / (x - 3)
    except ZeroDivisionError as e:
        logger.error(f"Error processing value {x}: {e}")
        return None

sc = SparkContext(appName="LoggingExample")
rdd = sc.parallelize([1, 2, 3, 4])
result = rdd.map(process_with_logging).collect()
