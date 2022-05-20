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

def eliminar_archivo():
    
    #Generamos la conexion con el metodo cursor
    cursor = conn.cursor()

    #Asignamos una variable para que el usuario pueda ingresar el id a localizar en la base de datos que quiere eliminar
    ingresar_id_a_eliminar = int(input("Ingresar id al cual quieras eliminar de la base de datos: "))
    
    sql = '''DELETE FROM archivos WHERE id = "{}" '''.format(ingresar_id_a_eliminar)
    
    #Ejecutamos el script pasandolo como parametro 
    cursor.execute(sql)
    
    #Imprimimos un mensaje que confirma el proceso exitoso
    print('ID: ', ingresar_id_a_eliminar, 'eliminado exitosamente, chequear en la base de datos por favor!')
    
    #Se commitea los cambios y se los sube a la base de datos
    conn.commit()
    
    #Se cierra la conexion a la base de datos   
    cursor.close()
    
#Se llama la funcion eliminar_archivo para su correcta ejecución    
eliminar_archivo()