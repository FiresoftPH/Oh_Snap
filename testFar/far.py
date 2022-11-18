#import streamlit as st
from flask import Flask, render_template, request, jsonify
import pyqrcode
import tkinter as tk
from PIL import ImageTk,Image  
import os
import png


def genQR():
    link = 'http://172.20.10.2:5000'
    url = pyqrcode.create(link)
    path = 'C:/Users/mrput/Documents/VSProject/Oh_Snap/Source/OhsnapQR/'
    os.chdir(path)
    url.png("qrcodela.png", scale=8)


def flasK():
    app = Flask(__name__, template_folder='template')

    @app.route("/", methods=['POST', 'GET'])
    def home():
        return render_template('display.html')

    app.run(debug = True)#, host='172.20.10.2')


def GuI():
    root = tk.Tk()
    root.title("OhSnap!")
    root.bind('<Escape>', lambda e: quit(e))
    #root.geometry()
    image = Image.open("C:/Users/mrput/Documents/VSProject/Oh_Snap/Source/OhsnapQR/qrcodela.png")
    test = ImageTk.PhotoImage(image)

    label1 = tk.Label(image=test, width = 700, height = 500)
    label1.pack()
    root.mainloop()
        

# def openst():
#     img_file = 'C:/Users/mrput/Documents/VSProject/OhsnapQR/Imgsavedinto'
#     for i in os.listdir(img_file):
#         print(i)


genQR()
#GuI()
flasK()
