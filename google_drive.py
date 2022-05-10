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
    resultado = []
    credenciales = login()
    lista_archivos = credenciales.ListFile({'q': query}).GetList()
    for lista in lista_archivos:
        # Fecha de ultima modificacion
        print('Fecha de ultima modificacion:',lista['modifiedDate'])
        # Version
        print('Version:',lista['version'])
        #extension
        print('Tipo de archivo:',lista['mimeType'])
        resultado.append(lista)
    
    return resultado

#================================================#

#Utilizamos metodo de creacion
if __name__ == "__main__":
    # crear_archivo_texto('Hola drive.txt', 'hola', '1Qn2162gOJsyTL4tOpa2KtVZFLPcKJZf9')
    busca("title =  'Hola drive'")

#===================================================#

    

    
    
    

