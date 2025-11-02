spark-submit \
  --master k8s://https://<KUBERNETES_API_SERVER> \
  --deploy-mode cluster \
  --name spark-pi \
  --class org.apache.spark.examples.SparkPi \
  local:///opt/spark/examples/jars/spark-examples.jar \
  100
