#!python3

import cv2
import numpy as np 
img = cv2.imread("firefox.png")

##BGR => Gray; gossie ; Canny

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussed = cv2.GaussianBlur(gray,(3,3),0)
cannyed = cv2.Canny(gaussed, 10 , 320)

cannyed2 = cv2.cvtColor(cannyed,cv2.COLOR_GRAY2BGR)

#colored

mask = cannyed > 0 #border
canvas = np.zeros_like(img) #draw paper
canvas[mask] = img[mask] #value

#sacw
res = np.hstack((img,cannyed2,canvas))#combine
cv2.imwrite("result.png",res)

cv2.imshow("canny in opencv",res)

key = 0xFF&cv2.waitKey(1000*10)
if key in (ord('Q'),ord('q'),27):
	print ("Exiting...")

cv2.destroyAllWindows()
