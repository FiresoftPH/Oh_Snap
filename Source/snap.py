# import cv2
# import os

# cam = cv2.VideoCapture(0)
# cv2.namedWindow("test")

# class Snap:
#     def __init__(self):
#         img_counter = 0
#         apath = "/home/pi/Documents/Project/Oh_Snap/Source/Imgsavedinto"
#         while True:
#             ret, frame = cam.read()
#             if not ret:
#                 print("failed to grab frame")
#                 break
#             cv2.imshow("test", frame)

#             key = cv2.waitKey(1)
#             # if k%256 == 27:
#             #     # ESC pressed
#             #     print("Escape hit, closing...")
#             #     break

#             if key%256 == 32:
#                 # SPACE pressed
#                 img_name = "opencvframe{}.jpg".format(img_counter)
#                 os.chdir(apath)
#                 cv2.imwrite(img_name, frame) #imshow
#                 print(img_name, "written!")
#                 #cv2.waitKey(0)

#                 img_counter += 1

#         cam.release()
#         cv2.destroyAllWindows

# # run = Snap()