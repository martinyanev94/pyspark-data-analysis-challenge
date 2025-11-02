import unittest
from pyspark.sql import SparkSession

class TestTransformations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("TestSparkApplication") \
            .getOrCreate()

    def test_transformation(self):
        input_data = [("Alice", 10), ("Bob", 20)]
        input_df = self.spark.createDataFrame(input_data, ["Name", "Value"])
        result_df = input_df.filter(input_df.Value > 10)
        self.assertEqual(result_df.count(), 1)  # Should return 1 row

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()
