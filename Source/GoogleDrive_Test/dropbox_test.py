#Access token
#sl.BTJTvAg71dF2bA4Who07btWN3Te_erWee4RKDZ0Q3-OofRgCuM2fK-8L-0PRTzbNR2QYRnLyVKgDY2hRbA1BXJsdbSgl08V7vCbOz1WI-tUfKsDhEcyb0JEPgBchnRNN9QpP66c
import dropbox

#Enter your own access token
dropbox_access_token = "<sl.BTJTvAg71dF2bA4Who07btWN3Te_erWee4RKDZ0Q3-OofRgCuM2fK-8L-0PRTzbNR2QYRnLyVKgDY2hRbA1BXJsdbSgl08V7vCbOz1WI-tUfKsDhEcyb0JEPgBchnRNN9QpP66c>"
dropbox_path = "/Ohsnap/Kyo.jpg"
computer_path = "c:\Users\Pim\OneDrive\Desktop\Oh_Snap\Source\GoogleDrive_Test\dropbox_test.py"

client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")

client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))