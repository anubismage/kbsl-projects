# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:03:35 2019

@author: anuja
"""

import cv2

import numpy as np

#img = np.zeros((512,512,3), np.uint8)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,200)
fontScale              = 0.6
fontColor              = (13,198,255)
lineType               = 2
img_rgb = cv2.imread("C:\ShadowlightFIles\\PythonFiles\\findpog.png")

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread("C:\ShadowlightFIles\\PythonFiles\\findme.png",0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
r=0
for pt in zip(*loc[::-1]):
    r=r+1
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (13,198,255), 1)

#cv.rectangle(img_rgb,r,5,(0,0),(255,0,0),2,lineType=LINE_8,true)
    cv2.putText(img_rgb,'Hello World!', 
        (pt[0] + w, pt[1] + h), 
        font, 
        fontScale,
        (13,198,255),
        lineType)
cv2.imshow('Detected',img_rgb)

print(r)
key = cv2.waitKey(0)
 # exit on ESC
cv2.destroyAllWindows()