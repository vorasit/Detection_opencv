import cv2
import os
cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imwrite('images/gun2.jpg', frame)
    os.system('python3 py_run_file.py')
    if(cv2.waitKey(1)&0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()