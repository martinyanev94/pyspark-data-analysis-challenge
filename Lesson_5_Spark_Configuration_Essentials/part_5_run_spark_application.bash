spark-submit \
    --class MySparkApp \
    --master yarn \
    --executor-memory 4g \
    --driver-memory 2g \
    --num-executors 5 \
    my_spark_application.py
