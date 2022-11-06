import streamlit as st
import pyqrcode
import tkinter as tk
from PIL import ImageTk,Image  
import os
import png

link = 'https://share.streamlit.io/785putt/movieselector/main/main.py'
url = pyqrcode.create(link)
url.png("qrcodela.png", scale=8)


# app = Flask(__name__)
# def flasK():
#     @app.route("/")
#     def hello_world(name="Napat"):
#         return 'Hello %s!' % name
#     app.run(debug = True) #host= '192.168.1.117'



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
    #     st.image(i)
    st.image('opencvframe0.jpg')

while True:
    #GuI()
    break
openst()