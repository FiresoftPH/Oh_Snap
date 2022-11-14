import cv2
import numpy as np

#Read the image
image = cv2.imread('Kyo.jpg')

#greyscale filter
def greyscale(image):
    greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return greyscale

#making the greyscale image
filter1 = greyscale(image)
filename = 'grey.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, filter1)

# brightness adjustment
def bright(image, beta_value ):
    img_bright = cv2.convertScaleAbs(image, beta=beta_value)
    return img_bright

#making the  more bright image
#positive beta value
filter2 = bright(image, 60)
filename = 'Bright.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, filter2)