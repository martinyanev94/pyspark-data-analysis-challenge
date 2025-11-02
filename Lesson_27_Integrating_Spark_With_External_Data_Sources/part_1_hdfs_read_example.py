from pyspark import SparkContext

sc = SparkContext(appName="HDFSReadExample")
hdfs_path = "hdfs://namenode:port/path/to/hdfs/file.txt"

data = sc.textFile(hdfs_path)
print(data.collect())
