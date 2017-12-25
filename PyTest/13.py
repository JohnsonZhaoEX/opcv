import cv2

img = cv2.imread('45.jpg',0)

rows,cols = img.shape
#set the first spot ,angle , scale)
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
#center
dst = cv2.warpAffine(img,M,(2*cols,2*rows))
while(1):
	cv2.imshow('img',dst)
	if cv2.waitKey(1)&0xFF == 27:
		break
cv2.destroyAllWindows()