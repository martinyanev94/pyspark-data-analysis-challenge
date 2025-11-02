conf.set("spark.driver.memory", "2g")\
    .set("spark.executor.instances", "5")
conf.set("spark.shuffle.compress", "true")\
    .set("spark.shuffle.spill.compress", "true")
