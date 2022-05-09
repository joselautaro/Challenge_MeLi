from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive




directory_credencials = 'credentials_module.json'

# Iniciar sesión
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directory_credencials)
# en el caso de que el token del archivo haya expirado, le decimos que cree uno nuevo y actualice el archivo
    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directory_credencials)
        # Caso contrario simplemente autorizamos
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)
print(login)

