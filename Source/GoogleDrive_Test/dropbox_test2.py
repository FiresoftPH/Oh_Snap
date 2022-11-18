#Access token
#sl.BTJTvAg71dF2bA4Who07btWN3Te_erWee4RKDZ0Q3-OofRgCuM2fK-8L-0PRTzbNR2QYRnLyVKgDY2hRbA1BXJsdbSgl08V7vCbOz1WI-tUfKsDhEcyb0JEPgBchnRNN9QpP66c
import dropbox
import sys

args = sys.argv
args_count = len(args)

if(args_count != 3):
    print('please input as: $ python %s fileLocal /fileNameDropBox' % args[0])
    quit()

f = open(args[1])

dbx = dropbox.Dropbox('sl.BTJTvAg71dF2bA4Who07btWN3Te_erWee4RKDZ0Q3-OofRgCuM2fK-8L-0PRTzbNR2QYRnLyVKgDY2hRbA1BXJsdbSgl08V7vCbOz1WI-tUfKsDhEcyb0JEPgBchnRNN9QpP66c')
dbx.files_upload(f, args[2])

f.close()