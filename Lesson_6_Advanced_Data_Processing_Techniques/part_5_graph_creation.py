from pyspark import SparkContext
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.graphx import Graph

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

# Define vertices in (id, attribute)
vertices = sc.parallelize([
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
])

# Define edges in (srcID, dstID, relationship)
edges = sc.parallelize([
    (1, 2, "follow"),
    (2, 3, "follow"),
    (1, 3, "follow"),
])

# Create a graph
graph = Graph(vertices, edges)

# Print out the vertices and edges
print("Vertices:")
print(graph.vertices.collect())
print("Edges:")
print(graph.edges.collect())
