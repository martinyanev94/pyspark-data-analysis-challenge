# Start the master
./sbin/start-master.sh

# Start worker nodes, replace with your worker IP addresses
./sbin/start-slave.sh spark://<master-ip>:7077
./bin/spark-submit \
    --class <main-class> \
    --master spark://<master-ip>:7077 \
    <your-application>.jar
