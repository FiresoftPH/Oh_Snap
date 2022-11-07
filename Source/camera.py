import cv2
import os
import mediapipe as mp
from customtkinter import CTkLabel, CTk
from PIL import Image, ImageTk
import time
from data_structure import Stack

class ShowFrame:
    def __init__(self):
        #Start cv2 video capturing through CSI port
        self.cap = cv2.VideoCapture(0)

        #Initialise Media Pipe Pose features
        self.mp_pose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose()
        # pose=mp_pose.Pose(model_complexity = 1)

        self.img_counter = 0
        self.apath = "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images"
        
        self.image_list = Stack([], 8)
        self.image_counter = 0

        self.stop_detect = False

    def detect_hand(self):

        self.stop_detect = False

        #Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
        while True:
            
            key = cv2.waitKey(1)
            if self.stop_detect == False:
                self.ret, self.frame = self.cap.read()
                self.flipped = cv2.flip(self.frame, flipCode = 0)
                self.frame1 = cv2.resize(self.flipped, (1280, 800))
                self.rgb_image = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2RGB)
                self.result = self.pose.process(self.rgb_image)

                # rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2BGR)
                # result=pose.process(rgb_img)
                # Print general details about observed body
                # print (result.pose_landmarks)
                
                #Uncomment below to see X,Y coordinate Details on single location in this case the Nose Location.
                
                try:
                    print('Shoulder: ', self.result.pose_landmarks.landmark[11].y * 1280)
                    print('Right Hand thing: ', self.result.pose_landmarks.landmark[19].y * 800)

                except: 
                    pass
                
                #Draw the framework of body onto the processed image and then show it in the preview window
                self.mpDraw.draw_landmarks(self.frame1, self.result.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

                # Show camera frames
                # cv2.imshow("frame", self.frame1)

            elif self.stop_detect == True or self.image_counter == 8:
                cv2.destroyWindow("Photo") 
                break
            
            # elif key % 256 == 27:
            #     # ESC pressed
            #     print("Escape hit, closing...")
            #     break

    def show_cam(self):

        self.stop_detect = True
        TIMER = int(5)
        
        prev = time.time()
        
        while TIMER >= 0:
            ret, img = self.cap.read()
            flip = cv2.flip(img, flipCode = 0)
            resize = cv2.resize(flip, (1280, 800))

            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(resize, str(TIMER),
                        (50, 50), font,
                        1, (0, 255, 255),
                        2, cv2.LINE_4)
            cv2.imshow('Photo', resize)
            cv2.waitKey(125)

            # current time
            cur = time.time()

            # Update and keep track of Countdown
            # if time elapsed is one second
            # than decrease the counter
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1

        else:
            ret, img = self.cap.read()
            flip = cv2.flip(img, flipCode = 0)
            resize = cv2.resize(flip, (1280, 800))

            # Display the clicked frame for 2
            # sec.You can increase time in
            # waitKey also
            cv2.imshow('Photo', resize)

            # time for which image displayed
            cv2.waitKey(2000)

            # Save the frame
            self.img_name = "Photo_{}.jpg".format(self.image_counter)
            os.chdir(self.apath)
            cv2.imwrite(self.img_name, resize) #imshow
            self.image_list.push(self.img_name)

            print(self.img_name, "written!")
            print(self.image_list.look())

            cv2.destroyWindow("Photo") 

            self.image_counter += 1

            return self.image_list