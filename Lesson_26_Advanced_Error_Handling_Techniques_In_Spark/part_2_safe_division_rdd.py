def safe_division(x):
    try:
        return 10 / (x - 3)
    except ZeroDivisionError:
        return None  # or some other default value indicating the error

transformation = rdd.map(safe_division)
result = transformation.collect()
print(result)
