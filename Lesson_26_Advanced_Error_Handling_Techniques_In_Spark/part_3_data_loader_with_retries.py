from retrying import retry

@retry(stop_max_attempt_number=3, wait_fixed=2000)
def load_data():
    # Placeholder for your data loading logic that might fail
    # For example, simulating a transient database connection error
    raise Exception("Simulated connection error")

rdd = sc.parallelize([1, 2, 3])

try:
    load_data()
except Exception as e:
    print(f"Failed to load data after retries: {e}")
