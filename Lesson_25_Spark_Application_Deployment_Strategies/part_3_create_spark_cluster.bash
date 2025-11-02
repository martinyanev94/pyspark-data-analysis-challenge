aws emr create-cluster \
    --name "Spark Cluster" \
    --release-label emr-5.30.0 \
    --applications Name=Spark \
    --ec2-attributes KeyName=<your-key-pair> \
    --instance-type m5.xlarge \
    --instance-count 3 \
    --use-default-roles
