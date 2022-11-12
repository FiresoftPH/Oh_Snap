import cv2
import numpy as np
import scipy

#Read the image
image = cv2.imread("IMG_6105[2182].jpg") # JUST A EXAMPLE IMG
#cv2.imshow('Show Result',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
 
#GRAYSCALE
def grayscale(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale 

#making the greyscale image
withfilter = grayscale(image)

# Saving the image
filename = 'GRAY.jpg'
cv2.imwrite(filename, withfilter)

#ADJUST BRIGHTNESS
def brightness(image, beta_value):
    brightness = cv2.convertScaleAbs(image, beta=beta_value)
    return brightness

withBright = brightness(image, 50)
filename = 'BRIGHT.jpg'
cv2.imwrite(filename, withBright)
