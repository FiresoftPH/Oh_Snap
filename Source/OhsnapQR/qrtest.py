#import streamlit as st
from flask import Flask, render_template
import pyqrcode
import tkinter as tk
from PIL import ImageTk,Image  
import os
import png

link = 'http://172.20.10.2:5000'
#link = 'http://127.0.0.1:5500/tss.html'
url = pyqrcode.create(link)
url.png("qrcodela.png", scale=8)


app = Flask(__name__)
def flasK():
    @app.route("/")
    def hello_world(name="Napat"):
        return 'Hello %s!' % name
    app.run(debug = True, host='172.20.10.2')



def GuI():
    root = tk.Tk()
    root.title("OhSnap!")
    root.bind('<Escape>', lambda e: quit(e))
    #root.geometry()
    image = Image.open("C:/Users/mrput/Documents/VSProject/OhsnapQR/qrcodela.png")
    test = ImageTk.PhotoImage(image)

    label1 = tk.Label(image=test, width = 700, height = 500)
    label1.pack()
    root.mainloop()
        
'''https://www.youtube.com/watch?v=VX1lmHaMAvo'''

def openst():
    img_file = 'C:/Users/mrput/Documents/VSProject/OhsnapQR/Imgsavedinto'
    # for i in os.listdir(img_file):
    #     print(i)

while True:
    GuI()
    flasK()
    break
