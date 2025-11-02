from pyspark.ml.evaluation import RegressionEvaluator

# Evaluating the model's performance
evaluator = RegressionEvaluator(labelCol="label_column", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE): {rmse}")

r2_evaluator = RegressionEvaluator(labelCol="label_column", predictionCol="prediction", metricName="r2")
r2 = r2_evaluator.evaluate(predictions)
print(f"R2: {r2}")
