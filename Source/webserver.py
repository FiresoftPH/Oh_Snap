from flask import Flask, render_template, request, jsonify
import pyqrcode
import tkinter as tk
from PIL import ImageTk,Image  
import os
import png

# Created by Puttipong (785putt)

# from main import cam
class Website:
    def genQR(self):
        link = 'http://172.20.10.3:5000'
        url = pyqrcode.create(link)
        path = '/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images'
        os.chdir(path)
        url.png("qrcodela.png", scale=8)


    def flasK(self):
        app = Flask(__name__, template_folder='template')

        @app.route("/", methods=['POST', 'GET'])
        def home():
            return render_template('display.html')

        app.run(host='172.20.10.3')#, host='172.20.10.2')


    def GuI(self):
        root = tk.Tk()
        root.title("OhSnap!")
        root.bind('<Escape>', lambda e: quit(e))
        #root.geometry()
        image = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/qrcodela.png")
        test = ImageTk.PhotoImage(image)

        label1 = tk.Label(image=test, width = 700, height = 500)
        label1.pack()
        root.mainloop()
        
    def clickbutton(self):
        root = tk.Tk()
        weid = tk.Label(root, text="Click button to run website")
        weid.pack()

        toclick = tk.Button(root, text="Click this", command = self.flasK)
        toclick.pack()
        root.mainloop()

# Website.genQR()
# app = Website()
# app.flasK()
# app.genQR()
# Website.flasK()
# Website.GuI()