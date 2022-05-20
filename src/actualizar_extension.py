#importo conector con lo que son los datos a la base de datos
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

#Determinamos el nombre de la función
def actualizar_extension():
    
    #Generamos la conexion con el metodo cursor
    cursor = conn.cursor()
    
    #Asignamos una variable para que el usuario pueda ingresar el id a localizar en la base de datos
    ingresar_nueva_extension = input("Ingrese nueva extension: ")
    
    #asignamos una variable para especificar la fecha nueva del id invocado
    ingresar_id_a_modificar = int(input("Ingrese el id al cual le quieras actualizar la extensión: "))
    
    #Genero el script SQL en este caso para actualizar tipo de extension en nuestra base de datos
    sql = '''UPDATE archivos SET extension = "{}" WHERE  id = "{}" '''.format(ingresar_nueva_extension, ingresar_id_a_modificar)
    
    #Ejecutamos el script SQL pasándolo como parámetro 
    cursor.execute(sql)
    
    #Imprimimos un mensaje que confirma el proceso exitoso
    print('Cambio de extensión exitosa a:', ingresar_nueva_extension, 'Chequear en la base de datos por favor!')
    
    #Subimos los cammbios a la base de datos
    conn.commit()
    
    #Se cierra la conexion a la base de datos   
    cursor.close()

#Activamos toda la función
actualizar_extension()