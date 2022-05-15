from email import message
from itertools import permutations
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import smtplib
from email.message import EmailMessage
#===========================================================================================#
# Iniciar sesión

credentials_directory = 'credentials_module.json'


def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credentials_directory)
    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(credentials_directory)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)


print(login)

#===============================================================================================#
# visualizar la hora del archivo


def search(query):
    result = []
    credenciales = login()
    list_file = credenciales.ListFile({'q': query}).GetList()
    for list in list_file:
        print('Fecha de ultima modificacion:', list['modifiedDate'])
        print('Version:', list['version'])
        print('Tipo de archivo:', list['mimeType'])
        result.append(list)

    return result


#================================================#
# Utilizamos metodo de creacion
if __name__ == "__main__":
    search("title =  'Hola drive'")

#===================================================#
# Eliminar permisos, exceptos el del owner


owner_email = 'desarrolladorjoselautaro@gmail.com'

file_id = '16d87oWGKbIax4JkHdRgZTkM6mlxwssEX'

credenciales = login()

file = credenciales.CreateFile({'id': file_id})
permutations_list = file.GetPermissions()
for obj in permutations_list:
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
