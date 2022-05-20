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
def actualizar_fecha_de_base_de_datos():
    
    #Generamos la conexion con el metodo cursor
    cursor = conn.cursor()
    
    #Asignamos una variable para que el usuario pueda ingresar el id a localizar en la base de datos
    ingresar_id_a_modificar = int(input("Ingresar id al cual le quieras actualizar en su fecha: "))
    
    #asignamos una variable para especificar la fecha nueva del id invocado
    ingresar_fecha_final = input("Ingresar nueva fecha: ")
    
    #Genero el script SQL en este caso para actualizar datos de ultima modificación en nuestra base de datos
    sql = '''UPDATE archivos SET ultimamodificacion = "{}" WHERE  id = "{}" '''.format(ingresar_fecha_final, ingresar_id_a_modificar)
    
    #Ejecutamos el script pasandolo como parametro 
    cursor.execute(sql)
    
    #Imprimimos un mensaje que confirma el proceso exitoso
    print('Cambio de fecha exitosa a: ', ingresar_fecha_final, 'Chequear en la base de datos por favor!')
    
    #Subimos los cammbios a la base de datos
    conn.commit()
    
    #Se cierra la conexion a la base de datos   
    cursor.close()

#Activamos toda la función
actualizar_fecha_de_base_de_datos()


