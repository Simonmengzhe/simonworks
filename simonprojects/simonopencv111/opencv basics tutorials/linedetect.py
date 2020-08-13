import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("Parameters")
cv2.createTrackbar("minlen", "Parameters", 50, 70, nothing)
cv2.createTrackbar("maxgap", "Parameters", 30, 90, nothing)
img = cv2.imread('rectangleline.jpg')
while (1):


    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 100
    maxLineGap = 20
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)



cv2.imshow('lines', img)

cv2.waitKey(0)
cv2.destroyAllWindows()