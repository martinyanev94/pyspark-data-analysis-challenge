spark-submit --master k8s://https://<K8S_API_SERVER> \
    --deploy-mode cluster \
    --name my_k8s_app \
    --class <MainClass> \
    --conf spark.some.config.option=config-value \
    my_spark_application.jar
