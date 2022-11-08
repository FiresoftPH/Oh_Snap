import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

dirc = 'C:/Users/mrput/Documents/VSproject/opencvframe{}.jpg'.format(img_counter)
apath = 'C:/Users/mrput/Documents/VSProject/OhsnapQR/Imgsavedinto'

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
        os.chdir(apath)
        cv2.imwrite(img_name, frame) #imshow
        print(img_name, "written!")
        #cv2.waitKey(0)
        
        img_counter += 1

cam.release()
cv2.destroyAllWindows()