import cv2
import numpy as np
#True when click mouse

drawing = False
#if mode is True ,draw the rectangle . press 'm' to draw curve

mode = True
ix,iy = -1,-1

#create the feedback function
def draw_circle(event , x, y, flags,param):
	global ix,iy,drawing,mode
	#click left bottom to bake to the default positon
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix ,iy =x,y
	elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
		if drawing ==True:
			if mode == True:
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
			else:
				#draw circle with dot ,3 stand the Width
				cv2.circle(img,(x,y),3,(0,0,255),-1)

	# stop draw when free the left mouse
	elif event == cv2.EVENT_LBUTTONUP:
		drawing == False

'''
bound the feedback function with opencv win , bound 'm' with mode shift  in main circle
'''
img = np.zeros((500,500,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1)&0xFF
	if k == ord('m'):
		mode = not mode
	elif k == ord('q'):
		break
cv2.destroyAllWindows()
