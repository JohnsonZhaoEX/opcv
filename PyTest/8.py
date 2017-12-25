import cv2
import numpy
img =cv2.imread('../Peace.jpg')
px = img[100,100]
print(px)
blue = img[100,100,0]
print(blue)
img[101,101]=[255,255,255]
print(img[101,101])