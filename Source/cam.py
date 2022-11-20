<<<<<<< HEAD
<<<<<<< Updated upstream
=======
>>>>>>> 49f45a72299767299101d1c81669e672c429b5fc
import cv2
import os
import tkinter as tk
from qrtest import Website

acpath = 'C:/Users/mrput/Desktop/Oh_Snap/testFar/static'
# THIS FILE MAY OR MAY NOT BE USE 
def cam():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencvframe{}.jpg".format(img_counter)
            os.chdir(acpath)
            cv2.imwrite(img_name, frame) #imshow
            print(img_name, "written!")
            #cv2.waitKey(0)
            
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

# root = tk.Tk()
# weid = tk.Label(root, text="Click button to run website")
# weid.pack()

# toclick = tk.Button(root, text="Click this", command=Website.flasK())
# toclick.pack()
<<<<<<< HEAD
=======
import cv2
import os
import tkinter as tk
from qrtest import Website

acpath = 'C:/Users/mrput/Desktop/Oh_Snap/testFar/static'
# THIS FILE MAY OR MAY NOT BE USE 
def cam():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencvframe{}.jpg".format(img_counter)
            os.chdir(acpath)
            cv2.imwrite(img_name, frame) #imshow
            print(img_name, "written!")
            #cv2.waitKey(0)
            
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

# root = tk.Tk()
# weid = tk.Label(root, text="Click button to run website")
# weid.pack()

# toclick = tk.Button(root, text="Click this", command=Website.flasK())
# toclick.pack()
>>>>>>> Stashed changes
=======
>>>>>>> 49f45a72299767299101d1c81669e672c429b5fc
# root.mainloop()