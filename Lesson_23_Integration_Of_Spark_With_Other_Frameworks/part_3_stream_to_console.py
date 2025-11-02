query = processedStreamDF.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
