jdbc_url = "jdbc:mysql://<hostname>:<port>/<dbname>"
properties = {
    "user": "<your_username>",
    "password": "<your_password>",
    "driver": "com.mysql.cj.jdbc.Driver"
}

df = spark.read.jdbc(url=jdbc_url, table="<your_table>", properties=properties)
