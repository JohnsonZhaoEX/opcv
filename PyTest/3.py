import numpy as np
import cv2

img = cv2.imread('../Peace.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()  #wait for ESC key to exit
elif k == ord('s'):
	cv2.imwrite('Peace_back.png',img)  #wait for 's' key to save and exit
	cv2.destoryAllWindows()
