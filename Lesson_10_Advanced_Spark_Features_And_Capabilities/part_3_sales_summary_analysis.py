sales_data = spark.read.csv("path/to/sales_data.csv", header=True, inferSchema=True)

# Group by 'product' and calculate the total sales for each product
sales_summary = sales_data.groupBy("product").agg({"amount": "sum"})

# Show the results
sales_summary.show()
