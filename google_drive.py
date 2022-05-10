from itertools import permutations
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


#===========================================================================================#

#autenticamos credenciales para no tener que volver a loguearse

directorio_de_credenciales = 'credentials_module.json'

# Iniciar sesión
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_de_credenciales)
# en el caso de que el token del archivo haya expirado, le decimos que cree uno nuevo y actualice el archivo
    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_de_credenciales)
        # Caso contrario simplemente autorizamos
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)
print(login)

#Crear un archivo de texto simple
def crear_archivo_texto(nombre_archivo, contenido, id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'title': nombre_archivo,
                                       'parents': [{'kind': 'drive#fileLink', 'id': id_folder}]})
    archivo.SetContentString(contenido)
    archivo.Upload()
    
#===============================================================================================#
    
#visualizar la hora del archivo

def busca(query):
    result = []
    credenciales = login()
    list_file = credenciales.ListFile({'q': query}).GetList()
    for list in list_file:
        # Fecha de ultima modificacion
        print('Fecha de ultima modificacion:',list['modifiedDate'])
        # Version
        print('Version:',list['version'])
        #extension
        print('Tipo de archivo:',list['mimeType'])
        result.append(list)
    
    return result

#================================================#

#Utilizamos metodo de creacion
if __name__ == "__main__":
    # crear_archivo_texto('Hola drive.txt', 'hola', '1Qn2162gOJsyTL4tOpa2KtVZFLPcKJZf9')
    busca("title =  'Hola drive'")

#===================================================#

#Eliminar permisos, exceptos el del owner

#Declaro en variable el mail del owner
owner_email = 'desarrolladorjoselautaro@gmail.com'
#declaro en variable el id del archivo al que deseo acceder
file_id = '16d87oWGKbIax4JkHdRgZTkM6mlxwssEX'
#Traigo las credenciales
credenciales = login()

#Declaro en una variable las credenciales y con la funcion Createfile designo que estamos hablando de este id para que autentifique
file = credenciales.CreateFile({'id': file_id})
#Traigo y declaro en una variable los permisos que tiene este archivo
permutations_list = file.GetPermissions()
#Recorro con un bucle citando la lista de permisos
for obj in permutations_list:
    #Si el objeto email es distinto a el mail del propietario
    if obj.get('emailAddress') != owner_email:
        #elimino el permiso de otros usuarios
        file.DeletePermission(obj['id'])
        
#=============================================================#
    
    

