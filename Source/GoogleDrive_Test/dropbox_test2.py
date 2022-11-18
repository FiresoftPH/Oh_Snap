#Access token
#sl.BTJTvAg71dF2bA4Who07btWN3Te_erWee4RKDZ0Q3-OofRgCuM2fK-8L-0PRTzbNR2QYRnLyVKgDY2hRbA1BXJsdbSgl08V7vCbOz1WI-tUfKsDhEcyb0JEPgBchnRNN9QpP66c
import dropbox

f = open('Kyo.jpg')

dbx = dropbox.Dropbox('sl.BTJTvAg71dF2bA4Who07btWN3Te_erWee4RKDZ0Q3-OofRgCuM2fK-8L-0PRTzbNR2QYRnLyVKgDY2hRbA1BXJsdbSgl08V7vCbOz1WI-tUfKsDhEcyb0JEPgBchnRNN9QpP66c')
dbx.files_upload(f, '/OhSnap')

f.close()