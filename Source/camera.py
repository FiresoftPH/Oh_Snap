import cv2
import os
import mediapipe as mp

#Start cv2 video capturing through CSI port
cap=cv2.VideoCapture(0)

#Initialise Media Pipe Pose features
mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose()
# pose=mp_pose.Pose(model_complexity = 1)

img_counter = 0
apath = "/home/pi/Documents/Project/Oh_Snap/Source/Imgsavedinto"

#Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
while True:
    key_1 = cv2.waitKey(1)
    key_2 = cv2.waitKey(1) & 0xFF
    if key_1 % 256 == 32:
        # SPACE pressed
        img_name = "opencvframe{}.jpg".format(img_counter)
        os.chdir(apath)
        cv2.imwrite(img_name, frame) #imshow
        print(img_name, "written!")
        #cv2.waitKey(0)

        img_counter += 1
    
    
    #At any point if the | q | is pressed on the keyboard then the system will stop
    elif key_2 == ord("q"):
        break

    ret,frame=cap.read()
    flipped=cv2.flip(frame,flipCode=1)
    frame1 = cv2.resize(flipped,(640,480))
    result = pose.process(frame1)

    # rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2BGR)
    # result=pose.process(rgb_img)
    #Print general details about observed body
    # print (result.pose_landmarks)
    
    #Uncomment below to see X,Y coordinate Details on single location in this case the Nose Location.
    
    try:
       print('Shoulder: ', result.pose_landmarks.landmark[11].y * 640)
       print('Right Hand thing: ', result.pose_landmarks.landmark[19].y * 480)
    except: 
       pass
    
    #Draw the framework of body onto the processed image and then show it in the preview window
    mpDraw.draw_landmarks(frame1,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow("frame",frame1)

    

    