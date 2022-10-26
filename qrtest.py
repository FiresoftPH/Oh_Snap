import qrcode
# from PIL import Image
# import requests
# from io import BytesIO

qr = qrcode.QRCode()
qr.add_data()
qr.make()
img = qr.make_image()
img.save('qrcode_test2.png')

# response = requests.get(url)
# img = Image.open(BytesIO(response.content))