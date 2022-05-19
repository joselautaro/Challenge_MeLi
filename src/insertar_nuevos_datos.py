#Importamos el módulo para conectar nuestraa base de datos con python
import mysql.connector

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

#iniciamos una funcion para hacer la carga de nuevos datos manuales
def insertar_nuevos_datos(id, nombres, extension, owner, visibilidad, ultimamodificacion):

     #Generamos la conexion con el metodo cursor
    cursor = conn.cursor()
    
    #Declaramos una variable para poder ingresar el número de id nuevo y parseamos mediante input
    ingresar_id = int(input("Ingresar id: "))
    
    #Declaramos una variable para poder asignarle un nombre al nuevo archivo mediante input
    nombre_del_archivo = input("Ingrese nombre del archivo: ")
    
    #Declaramos una variable la cual vamos a poder usar para ingresar un tipo de extensión mediante input
    ingresar_extension = input("Ingresar tipo de extension, ¿.excel, .doc o .txt?: ")
    
    #Declaramos una variable para asignar un tipo de propietario mediante input
    tipo_de_propietario = input("¿Owner o invitado/a?: ")
    
    #Delaramos una variable para el estado del archivo
    estado_de_archivo = input("Estado de archivo, ¿privado o público?: ")
    
    #Delaramos una variable para asignar una fecha
    ingresar_fecha = input("Ingresar fecha: ")
    
    #Mediante instrucción SQL para poder efecutar los ingresos a nuestra base de datos pasado como parámetro cada una de las variables asignadas anteriormente
    sql='''INSERT INTO archivos (id, nombres, extension, owner, visibilidad, ultimamodificacion)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(ingresar_id, nombre_del_archivo, ingresar_extension, tipo_de_propietario, estado_de_archivo, ingresar_fecha)

    #Genero el cursor execute para que nuestro comando SQL se ejecute y se vea en la base de datos
    cursor.execute(sql)
    
    #Generamos la conexión con conn y con el commit le damos el ok para que se suba a nuestra base de datos
    conn.commit()
    
    #Cerramos la conexión con la base de datos
    cursor.close()
    
    
    
#Activamos nuestra función
insertar_nuevos_datos('id', 'nombres', 'extension', 'owner', 'visibilidad', 'ultimamodificacion')






