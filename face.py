# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

#video = cv2.VideoCapture(0)

a = 1
img= cv2.imread("C:\Users\\anuja\\Desktop\\pics\\xqcHAIR.png",1)
face_cascade = cv2.CascadeClassifier('C:\ShadowlightFIles\\haarcascade_frontalface_default.xml')
#cv2.imshow("example",img)
while True :
    a=a+1
    check,frame = img.read()
    print(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # cv2.imshow("Capturehmm",gray)
    faces = face_cascade.detectMultiScale(gray,	scaleFactor = 1.1, minNeighbors = 5)
for (x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]    
    roi_color = img[y:y+h, x:x+w]
    cv2.imshow("img",gray)
    key = cv2.waitKey(1)
    if key == ord("q") :
        break
print(a)

#video.release()
cv2.destroyAllWindows()