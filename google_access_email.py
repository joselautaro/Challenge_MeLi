from email import message
from itertools import permutations
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import smtplib
from email.message import EmailMessage
#===========================================================================================#
# Iniciar sesión

#Establecemos una variable en donde llamamos a las credenciales
directorio_de_credenciales = 'credentials_module.json'

#Establecemos una funcion, donde las credenciales se refrescan en caso de que expiren
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_de_credenciales)
    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_de_credenciales)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)

#===============================================================================================#
# visualizar la hora del archivo

#Establecemos una funcion donde 
def buscar(query):
    resultado = []
    credenciales = login()
    lista_de_archivo = credenciales.ListFile({'q': query}).GetList()
    for list in lista_de_archivo:
        print('Fecha de ultima modificacion:', list['modifiedDate'])
        print('Version:', list['version'])
        print('Tipo de archivo:', list['mimeType'])
        resultado.append(list)

    return resultado


#================================================#
# Utilizamos metodo de creacion
if __name__ == "__main__":
    #Ejecutando la funcion buscar
    buscar("title =  'Hola drive'")

#===================================================#
# Eliminar permisos, exceptos el del owner

#establecemos una variable con el mail del owner
email_propietario = 'desarrolladorjoselautaro@gmail.com'

#Establecemos una variable con identrificador unico del archivo
identificador_de_archivo = '16d87oWGKbIax4JkHdRgZTkM6mlxwssEX'

#Iniciamos con las credenciales que estan en la función login
credenciales = login()

#establecemos una variable file a la que le pasamos las credenciales necesarias y el metodo Createfile con la variable que tiene el identificador
archivo = credenciales.CreateFile({'id': identificador_de_archivo})

#Se establece una variable para definir la lista de permisos llamando al metodo Get
lista_de_permisos = archivo.GetPermissions()

#Se recorre con un bucle for la lista de permisos y en el caso de que el id de los permisos sea diferente al del owner, se elimina el permiso y se convierte el archivo privado
for obj in lista_de_permisos:
    if obj.get('emailAddress') != email_propietario:
        archivo.DeletePermission(obj['id'])

print("El archivo pasa a ser privado y se le enviará un mail al owner, notificando dicho cambio.")

#=============================================================#

# Enviamos mail al owner, notificando el cambio  de visibilidad
mensaje = EmailMessage()

#Establecemos el asunto del mail
asunto_del_mail = "Hola, te hablamos desde App-Python🙌"

#Establecemos el correo del cual se enviará el mail
correo_mail_saliente = "joselautarom@gmail.com"

#Establecemos el correo que recepcionará el mail
correo_mail_entrante = "desarrolladorjoselautaro@gmail.com"


#Establecemos carcateristicas de las variables declaradas arriba
mensaje['Subject'] = asunto_del_mail
mensaje['From'] = correo_mail_saliente
mensaje['To'] = correo_mail_entrante

#Agremos el contenido del mail
mensaje.set_content(
    "El usuario con el que compartes este archivo fue eliminado y pasa a estado privado!")

#Conectamos con el servidor
email_smtp = "smtp.gmail.com"
server = smtplib.SMTP(email_smtp, '587')
email_smtp = "smtp.gmail.com"

server = smtplib.SMTP(email_smtp, '587')

server.ehlo()

server.starttls()

#Logueamos el mail y contraseña usada para este usuario
correo_mail_saliente = "joselautarom@gmail.com"
password_email = "jpasztgvtzldwknb"

#Logueamos el envio y recepcion del mail
server.login(correo_mail_saliente, password_email)

server.send_message(mensaje)

#Cerramos la conexion con el servidor del mail
server.quit()

#Imprimimos mensaje para el usuario
print("Envío exitoso, por favor consulte con el owner!")
