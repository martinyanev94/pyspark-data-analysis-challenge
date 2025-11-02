kubectl run your-spark-app \
    --image=<your-spark-image> \
    -- \
    spark-submit \
    --master k8s://https://<kube-master-ip> \
    --deploy-mode cluster \
    --name your-spark-app \
    --class <main-class> \
    <your-application>.jar
