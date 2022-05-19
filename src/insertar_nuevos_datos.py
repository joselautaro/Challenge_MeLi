import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="mydrive"
)

def insertar_nuevos_datos(id, nombres, extension, owner, visibilidad, ultimamodificacion):
    
    cursor = conn.cursor()
    ingresar_id = int(input("Ingresar id: "))
    nombre_del_archivo = input("Ingrese nombre del archivo: ")
    ingresar_extension = input("Ingresar tipo de extension, ¿.excel, .doc o .txt?: ")
    tipo_de_propietario = input("¿Owner o invitado/a?: ")
    estado_de_archivo = input("Estado de archivo, ¿privado o público?: ")
    ingresar_fecha = input("Ingresar fecha: ")
    sql='''INSERT INTO archivos (id, nombres, extension, owner, visibilidad, ultimamodificacion)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(ingresar_id, nombre_del_archivo, ingresar_extension, tipo_de_propietario, estado_de_archivo, ingresar_fecha)
    
    cursor.execute(sql)
    n=cursor.rowcount
    conn.commit()    
    cursor.close()

insertar_nuevos_datos('id', 'nombres', 'extension', 'owner', 'visibilidad', 'ultimamodificacion')