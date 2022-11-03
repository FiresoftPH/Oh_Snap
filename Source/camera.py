import cv2
import os
import mediapipe as mp
from customtkinter import CTkLabel, CTk
from PIL import Image, ImageTk

window = CTk()
window.geometry("640x400")

class ShowFrame:
    def __init__(self, frame):
        #Start cv2 video capturing through CSI port
        self.cap = cv2.VideoCapture(0)

        #Initialise Media Pipe Pose features
        self.mp_pose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose()
        # pose=mp_pose.Pose(model_complexity = 1)

        self.img_counter = 0
        self.apath = "/home/pi/Documents/Project/Oh_Snap/Source/Imgsavedinto"

        self.frame = frame
        self.opencv_image = CTkLabel(frame)
        self.opencv_image.grid(row=0, column=0)
        
        # self.ret, self.frame = self.cap.read()
        # self.flipped = cv2.flip(self.frame, flipCode = 1)
        # self.frame1 = cv2.resize(self.flipped, (640, 480))
        # self.result = self.pose.process(self.frame1)

    def detect_hand(self):
        #Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
        while True:
            
            text = "TutorialsPoint"
            coordinates = (100,100)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255,0,255)
            thickness = 2
            image = cv2.putText(image, text, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)

            self.key_1 = cv2.waitKey(1)
            self.key_2 = cv2.waitKey(1) & 0xFF
            if self.key_1 % 256 == 32:
                # SPACE pressed
                self.img_name = "opencvframe{}.jpg".format(self.img_counter)
                os.chdir(self.apath)
                cv2.imwrite(self.img_name, self.frame) #imshow
                print(self.img_name, "written!")
                #cv2.waitKey(0)

                self.img_counter += 1
            
            
            #At any point if the | q | is pressed on the keyboard then the system will stop
            elif self.key_2 == ord("q"):
                break

            self.ret, self.frame = self.cap.read()
            self.flipped = cv2.flip(self.frame, flipCode = 1)
            self.frame1 = cv2.resize(self.flipped, (640, 480))
            self.result = self.pose.process(self.frame1)

            # rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2BGR)
            # result=pose.process(rgb_img)
            # Print general details about observed body
            # print (result.pose_landmarks)
            
            #Uncomment below to see X,Y coordinate Details on single location in this case the Nose Location.
            
            try:
                print('Shoulder: ', self.result.pose_landmarks.landmark[11].y * 640)
                print('Right Hand thing: ', self.result.pose_landmarks.landmark[19].y * 480)

            except: 
                pass
            
            #Draw the framework of body onto the processed image and then show it in the preview window
            self.mpDraw.draw_landmarks(self.frame1, self.result.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

            # Show camera frames
            cv2.imshow("frame", self.frame1)

    def show_tkinter(self):
        self.key_1 = cv2.waitKey(1)
        if self.key_1 % 256 == 32:
            # SPACE pressed
            self.img_name = "opencvframe{}.jpg".format(self.img_counter)
            os.chdir(self.apath)
            cv2.imwrite(self.img_name, self.frame) #imshow
            print(self.img_name, "written!")
            #cv2.waitKey(0)

            self.img_counter += 1

        cv2image= cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        self.opencv_image.imgtk = imgtk
        self.opencv_image.configure(image=imgtk)
        self.opencv_image.after(60, self.show_tkinter)

app = ShowFrame(window)
app.show_tkinter()
window.mainloop()