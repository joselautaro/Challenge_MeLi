#importo conector con lo que son los datos a la base de datos
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
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
    #Genero el script SQL en este caso para actualizar datos en nuestra base de datos
    sql = '''UPDATE archivos SET ultimamodificacion = "{}" WHERE  id = "{}" '''.format(ingresar_fecha_final, ingresar_id_a_modificar)
    #Imprimimos un mensaje que confirma el proceso exitoso
    print("Cambio de fecha modificada, exitosa!")
    #Ejecutamos el script pasandolo como parametro 
    cursor.execute(sql)
    # n=cursor.rowcount
    conn.commit()
    #Se cierra la conexion a la base de datos   
    cursor.close()

#Activamos toda la función
actualizar_fecha_de_base_de_datos()
