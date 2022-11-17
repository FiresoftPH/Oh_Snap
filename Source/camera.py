import cv2
import os
import mediapipe as mp
from customtkinter import CTkLabel, CTk
from PIL import Image, ImageTk
import time
from data_structure import Stack

# Created by Pattarapark Chutisamoot (FiresoftGH) and Puttipong Aunggulsant (785putt)

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
        self.confidence = None
        self.first_pose_bool = None
        self.second_pose_bool = None

        self.stop_detect = False

    def detect_hand(self):

        self.stop_detect = False
        initial_time = time.time()
        #Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
        while self.image_list.size() < 8:
            
            key = cv2.waitKey(1)
            if self.stop_detect == False:
                self.ret, self.frame = self.cap.read()
                self.flipped = cv2.flip(self.frame, flipCode = 1)
                self.frame1 = cv2.resize(self.flipped, (640, 400))
                self.rgb_image = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2RGB)
                self.result = self.pose.process(self.rgb_image)

                # rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2BGR)
                # result=pose.process(rgb_img)
                # Print general details about observed body
                # print (result.pose_landmarks)
                
                try:
                # Uncomment below to see X,Y coordinate Details on single location in this case the Nose Location.
                    right_shoulder =  self.result.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_SHOULDER].y * 400
                    right_hand = self.result.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_INDEX].y * 400
                    
                    # Tracking Integrity to avoid other poses
                    track_integrity = self.result.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_INDEX].x * 640
                    # print('Right Shoulder: ', right_shoulder)
                    # print('Right Hand thing: ', right_hand)
                    print('Intergrity Count: ', track_integrity)
                    
                    if track_integrity >= 430 and track_integrity < 480:
                        self.confidence = True
                        print("Ready to Track")

                    if right_shoulder - right_hand >= 50 and self.confidence == True:
                        self.first_pose_bool = True
                        print("Hand Raised")

                    if right_shoulder - right_hand <= -50 and self.first_pose_bool == True:
                        self.second_pose_bool = True
                        print("Hand Down after Hand Raised")

                    if self.first_pose_bool == True and self.second_pose_bool == True:
                        self.show_cam()

                    current_time = time.time()
                    if current_time - initial_time >= 0.5 :
                        self.first_pose_bool = False
                        self.second_pose_bool = False
                        self.coinfidence = False
                        print("Variable Reset")
                        initial_time = time.time()
                    
                    #Draw the framework of body onto the processed image and then show it in the preview window
                    self.mpDraw.draw_landmarks(self.frame1, self.result.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)


                    # Show camera frames
                    # cv2.imshow("frame", self.frame1)
                
                except:
                    pass

            elif self.stop_detect == True or self.image_counter == 8:
                cv2.destroyWindow("Photo") 
                break
            
            elif key % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break

    def show_cam(self):

        self.stop_detect = True
        TIMER = int(3)
        
        prev = time.time()
        
        while TIMER >= 0:
            ret, img = self.cap.read()
            flip = cv2.flip(img, flipCode = 1)
            resize = cv2.resize(flip, (1280, 800))

            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(resize, str(TIMER),
                        (50, 120), font,
                        3, (0, 255, 255),
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
            flip = cv2.flip(img, flipCode = 1)
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

            self.stop_detect = False

            return self.image_list

    def close_all(self):
        self.stop_detect = True
