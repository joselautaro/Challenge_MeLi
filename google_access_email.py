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


print(login)

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
owner_email = 'desarrolladorjoselautaro@gmail.com'

#Establecemos una variable con identrificador unico del archivo
file_id = '16d87oWGKbIax4JkHdRgZTkM6mlxwssEX'

#Iniciamos con las credenciales que estan en la función login
credenciales = login()

#establecemos una variable file a la que le pasamos las credenciales necesarias y el metodo Createfile con la variable que tiene el identificador
file = credenciales.CreateFile({'id': file_id})

#Se establece una variable para definir la lista de permisos llamando al metodo Get
lista_de_permisos = file.GetPermissions()

#Se recorre con un bucle for la lista de permisos y en el caso de que el id de los permisos sea diferente al del owner, se elimina el permiso y se convierte el archivo privado
for obj in lista_de_permisos:
    if obj.get('emailAddress') != owner_email:
        file.DeletePermission(obj['id'])

print("El archivo pasa a ser privado y se le enviará un mail al owner, notificando dicho cambio.")

#=============================================================#

# Enviamos mail al owner, notificando el cambio  de visibilidad
message = EmailMessage()


email_subject = "Hola, te hablamos desde App-Python🙌"
sender_email_address = "joselautarom@gmail.com"
receiver_email_addres = "desarrolladorjoselautaro@gmail.com"

message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_addres

message.set_content(
    "El usuario con el que compartes este archivo fue eliminado y pasa a estado privado!")

email_smtp = "smtp.gmail.com"
server = smtplib.SMTP(email_smtp, '587')
email_smtp = "smtp.gmail.com"

server = smtplib.SMTP(email_smtp, '587')

server.ehlo()

server.starttls()

sender_email_address = "joselautarom@gmail.com"

email_password = "jpasztgvtzldwknb"

server.login(sender_email_address, email_password)

server.send_message(message)

server.quit()

print("Envío exitoso, por favor consulte con el owner!")
