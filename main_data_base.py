from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Bienvenidos/as a mi app challenge de python!"
app.run(host="0.0.0.0")
#Importamos el modulo para la conexion a la base de datos
import mysql.connector
import os


#Se establace conexion a la base de datos
conn = mysql.connector.connect(
    
    #Determinamos el tipo del host
    host="localhost",
    
    #Asignamos un usuario tipo root
    user="root",
    
    #Determinamos el password de nuestra base
    password="",
    
    #Determinamos el puesto (Es el que viene por default)
    port="3306",
    
    #Nombre de nuestra base de datos
    database="mydrive"
)

#Generamos la conexion a la base de datos con el metodo cursor
cursor = conn.cursor()

#Declaramos el nombre de la función
def crear_base_de_datos():
    
    #Se crea tabla archivos
    sql = """CREATE TABLE archivos (id INT AUTO_INCREMENT, nombres VARCHAR(255), extension VARCHAR(255), owner VARCHAR(255), visibilidad VARCHAR(255), ultimamodificacion VARCHAR(255))"""
    
    #Se insertan datos en la tabla archivos mediante una lista de tuplas
    sql = """INSERT INTO archivos (id, nombres, extension, owner, visibilidad, ultimamodificacion) VALUES(%s, %s, %s, %s, %s, %s)"""
    
    #Se genera un lista de tuplas con diferentes datos inciales
    valores = [
        ("", "resume pombo", ".docs", "José Lautaro Desarrollador", "privado", "3/5/2022"),
        ("", "Reforma Universitaria de1918", ".docs", "José Lautaro Desarrollador", "privado", "6/5/2022"),
        ("", "INFOHOST.txt", ".txt", "José Lautaro Desarrollador", "privado", "26/2/2022"),
        ("", "Presupuesto", ".docs", "José Lautaro Desarrollador", "privado", "3/3/2022"),
        ("", "Unidad 4 -", ".docs", "José Lautaro Desarrollador", "privado", "8/3/2022"),
        ("", "Capitulo 2 IVU", ".docs", "José Lautaro Desarrollador", "privado", "5/3/2022"),
    ]
    
    #con el executemany podemos ejecutar una instrucción que sale de una lista de tuplas SQL 
    cursor.executemany(sql, valores)

#Activamos nuestra funcion crear base de datos
crear_base_de_datos()

#Commiteamos todos los datos a nuestra base de datos mydrive
conn.commit()

#Cerramos la conexion con el servidor
conn.close()