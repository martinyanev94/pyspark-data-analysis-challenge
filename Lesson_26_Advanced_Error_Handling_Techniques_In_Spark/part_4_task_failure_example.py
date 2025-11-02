from pyspark import SparkContext

sc = SparkContext(appName="TaskFailureExample")

failure_count = sc.accumulator(0)

def process_data(x):
    global failure_count
    if x == 2:
        failure_count += 1
        raise Exception("Simulated failure")
    return x * 10

rdd = sc.parallelize([1, 2, 3, 4])
try:
    result = rdd.map(process_data).collect()
except Exception as e:
    print(f"Caught an error: {e}")

print(f"Total failures encountered: {failure_count.value}")
