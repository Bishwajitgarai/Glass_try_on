#All the imports go here
# from turtle import width
import numpy as np
import cv2
import time

#Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('A:/work space/face/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('A:/work space/face/haarcascade_eye_tree_eyeglasses.xml')
glass_color=(0, 0, 0)
#Variable store execution state
first_read = True

#Starting the video capture
cap = cv2.VideoCapture(0)
ret,img = cap.read()

while(ret):
	ret,img = cap.read()
	img=cv2.flip(img,1,1)
	time.sleep(0.01)
	#Converting the recorded image to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#Applying filter to remove impurities
	gray = cv2.bilateralFilter(gray,5,1,1)

	#Detecting the face for region of image to be fed to eye classifier
	faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200))
	if(len(faces)>0):
		for (x,y,w,h) in faces:
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

			#roi_face is face which is input to eye classifier
			roi_face = gray[y:y+h,x:x+w]
			roi_face_clr = img[y:y+h,x:x+w]
			eyes = eye_cascade.detectMultiScale(img, scaleFactor = 1.2,minNeighbors = 4)
			count=0
			startpoint=0
			endpoint=0
			height=0
			wheight=0 
			if(len(eyes)%2==0):
					for (ex,ey,ew,eh) in eyes:
						count=count+3
						if count%2!=0:
							startpoint=(ex+ew,(ey+(eh//2)))
							startpoint2=(ex,ey+(eh//2))
							height=ew
						else:
							endpoint=(ex,ey+(eh//2))
							endpoint2=(ex+ew,ey+(eh//2))
							wheight=ew
                            
						# cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255, 0, 0),2)
						cv2.circle(img,(ex+(ew//2),ey+(eh//2)),27,(255,206,68),-1)
						cv2.circle(img,(ex+(ew//2),ey+(eh//2)),28,(255,0,0),2)
						if startpoint!=0 and endpoint!=0:
								

								if(startpoint[0]-endpoint[0])<0:
                                    
									if(height<wheight):
										if wheight-height<5:
											cv2.line(img,endpoint2,((endpoint2[0]+20,endpoint2[1]-10)),glass_color,2)
											cv2.line(img,startpoint2,(startpoint2[0]-20,startpoint2[1]-10),glass_color,2)
										else:
											cv2.line(img,endpoint2,((endpoint2[0]+50,endpoint2[1]-20)),glass_color,2)
											cv2.line(img,startpoint2,(startpoint2[0]-10,startpoint2[1]-10),glass_color,2)
									else:
										if height-wheight<5:
											cv2.line(img,endpoint2,((endpoint2[0]+20,endpoint2[1]-10)),glass_color,2)
											cv2.line(img,startpoint2,(startpoint2[0]-20,startpoint2[1]-10),glass_color,2)
											
										else:
											cv2.line(img,(endpoint2),((endpoint2[0]+15,endpoint2[1]-10)),glass_color,2)
											cv2.line(img,startpoint2,(startpoint2[0]-50,startpoint2[1]-20),glass_color,2)

									cv2.line(img,startpoint,endpoint,glass_color,2)
								else:
									if height>wheight:
										if height-wheight<5 :
											cv2.line(img,startpoint,(startpoint[0]+20,startpoint[1]-10),glass_color,2)
											cv2.line(img,endpoint,(endpoint[0]-20,endpoint[1]-10),glass_color,2)
										else:
											cv2.line(img,startpoint,(startpoint[0]+50,startpoint[1]-20),glass_color,2)
											cv2.line(img,endpoint,(endpoint[0]-10,endpoint[1]-10),glass_color,2)
									else:
										if wheight-height<5 :
											cv2.line(img,startpoint,(startpoint[0]+20,startpoint[1]-10),glass_color,2)
											cv2.line(img,endpoint,(endpoint[0]-20,endpoint[1]-10),glass_color,2)
										else:
											cv2.line(img,endpoint,(endpoint[0]-50,endpoint[1]-20),glass_color,2)
											cv2.line(img,startpoint,(startpoint[0]+10,startpoint[1]-10),glass_color,2) 
									cv2.line(img,endpoint2,startpoint2,glass_color,2)
									
	#Controlling the algorithm with keys
	cv2.imshow('img',img)
	a = cv2.waitKey(1)
	if(a==ord('q')):
		break
	
cap.release()
cv2.destroyAllWindows()





