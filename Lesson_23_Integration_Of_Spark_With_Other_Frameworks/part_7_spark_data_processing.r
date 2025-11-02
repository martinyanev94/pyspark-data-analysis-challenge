library(sparklyr)

# Connecting to Spark
sc <- spark_connect(master = "local")

# Read data in R
spark_df <- spark_read_csv(sc, name = "example_data", path = "input_data.csv", header = TRUE)

# Perform operations using dplyr syntax
spark_df %>%
  filter(some_column > threshold) %>%
  collect()
