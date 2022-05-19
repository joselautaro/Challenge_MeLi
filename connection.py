from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json debe estar en el mismo directorio que el script
drive = GoogleDrive()