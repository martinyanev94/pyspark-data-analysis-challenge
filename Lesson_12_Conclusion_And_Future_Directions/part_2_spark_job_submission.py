import requests

# Define the endpoint for submitting a Spark job
url = "http://spark-cluster-url:8080/spark-submit"

# Prepare the JSON payload
payload = {
    "appName": "Data Processing Job",
    "file": "hdfs://path/to/your/app.py",
    "class": "YourMainClass",
    "sparkArgs": ["--executor-memory", "4g", "--num-executors", "4"]
}

# Submit the Spark job via a POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    print("Job submitted successfully")
else:
    print("Error submitting job:", response.text)
