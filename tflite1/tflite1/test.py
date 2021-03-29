import numpy as np
import cv2
import imutils
import datetime
import os 
gun_cascade=cv2.CascadeClassifier('cascade.xml')
camera=cv2.VideoCapture(0)

firstFrame=None

gun_exist=False
while True:
    (grabbed,frame)=camera.read()

    if not grabbed:
        break

    frame=imutils.resize(frame,width=500)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    gun=gun_cascade.detectMultiScale(gray,1.3,5,minSize=(100,100))

    if len(gun)>0:
        gun_exist=True

    for (x,y,w,h) in gun:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

    if firstFrame is None:
        firstFrame=gray
        continue
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10,frame.shape[0]-10),font,0.35,(0,0,255),1)

    cv2.imshow("Security Feed",frame)
    if(cv2.waitKey(1)&0xFF == ord('q')):
        break

if gun_exist:
    print("gun detected")
else:
    print("gun Not detected")

camera.release()
cv2.destroyAllWindows()