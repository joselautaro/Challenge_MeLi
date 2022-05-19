#importo conector con lo que son los datos a la base de datos
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="mydrive"
)

