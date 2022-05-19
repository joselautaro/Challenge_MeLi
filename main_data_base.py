from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Bienvenidos/as a mi app challenge de python!"

import mysql.connector
import os

app.run(host="0.0.0.0")
#Se establace conexion a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="mydrive"
)
cursor = conn.cursor()

def crear_base_de_datos():
    #Se crea tabla archivos
    sql = """CREATE TABLE archivos (id INT AUTO_INCREMENT, nombres VARCHAR(255), extension VARCHAR(255), owner VARCHAR(255), visibilidad VARCHAR(255), ultimamodificacion VARCHAR(255))"""
    #Se insertan datos en la tabla archivos mediante una lista de tuplas
    sql = """INSERT INTO archivos (id, nombres, extension, owner, visibilidad, ultimamodificacion) VALUES(%s, %s, %s, %s, %s, %s)"""

    valores = [
        ("", "resume pombo", ".docs", "José Lautaro Desarrollador", "privado", "3/5/2022"),
        ("", "Reforma Universitaria de1918", ".docs", "José Lautaro Desarrollador", "privado", "6/5/2022"),
        ("", "INFOHOST.txt", ".txt", "José Lautaro Desarrollador", "privado", "26/2/2022"),
        ("", "Presupuesto", ".docs", "José Lautaro Desarrollador", "privado", "3/3/2022"),
        ("", "Unidad 4 -", ".docs", "José Lautaro Desarrollador", "privado", "8/3/2022"),
        ("", "Capitulo 2 IVU", ".docs", "José Lautaro Desarrollador", "privado", "5/3/2022"),
    ]
    cursor.executemany(sql, valores)
    
crear_base_de_datos()

conn.commit()
for bd in cursor:
    print(bd)
conn.close()