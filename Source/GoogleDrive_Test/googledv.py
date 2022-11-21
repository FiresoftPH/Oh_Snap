from googleapiclient.http import MediaFileUpload
from Google import create_service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Upload a file
file_metadata = {
    'name': 'drink.png',
    'parents': ['<folder id 1>', '<folder id 2>']
}

media_content = MediaFileUpload('coffee.png', mimetype='image/png')

file = service.files().create(
    body=file_metadata,

    media_body=media_content
).execute()

print(file)


# Replace Existing File on Google Drive
file_id = '<file id>'

media_content = MediaFileUpload('mp4.png', mimetype='image/png')

service.files().update(
    fileId=file_id,
    media_body=media_content
).execute()