jdbc_url = "jdbc:mysql://your-database-url:3306/your_database"
properties = {
     "user": "your_username",
     "password": "your_password",
     "driver": "com.mysql.cj.jdbc.Driver"
}

query = "(SELECT * FROM your_table) AS tmp"
df_mysql = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)
df_mysql.show()
