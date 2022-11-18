#1J6WzZyxidbrF7IsuK9SMsC0BXFEjr5SD

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

upload_file_list = ['C:\Users\Pim\OneDrive\Desktop\Oh_Snap\Source\GoogleDrive_Test\Kyo.jpg']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1J6WzZyxidbrF7IsuK9SMsC0BXFEjr5SD'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.