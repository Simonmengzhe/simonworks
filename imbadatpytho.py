
import cv2
import numpy as np
from locating_the_plane_and_drawing_it import finding_blue


def nothing(x):
    pass

cv2.namedWindow("Parameters", cv2.WINDOW_NORMAL)
cv2.createTrackbar("L_A", "Parameters", 0, 255, nothing)
cv2.createTrackbar("L_B", "Parameters", 0, 255, nothing)
cv2.createTrackbar("L_C", "Parameters", 0, 255, nothing)
cv2.createTrackbar("H_A", "Parameters", 1, 255, nothing)
cv2.createTrackbar("H_B", "Parameters", 1, 255, nothing)
cv2.createTrackbar("H_C", "Parameters", 1, 255, nothing)

#import videocapture
cap0 = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture(0)



while(1):

    la = cv2.getTrackbarPos("L_A", "Parameters")
    lb = cv2.getTrackbarPos("L_B", "Parameters")
    lc = cv2.getTrackbarPos("L_C", "Parameters")
    ha = cv2.getTrackbarPos("H_A", "Parameters")
    hb = cv2.getTrackbarPos("H_B", "Parameters")
    hc = cv2.getTrackbarPos("H_C", "Parameters")

    lower_black = np.array([la, lb, lc])
    upper_black= np.array([ha, hb, hc])

    # Take each frame and blur
    _,frameunblurred0 = cap0.read()
    frameunblurred0 = frameunblurred0[60:400,:,:]

    mask = finding_blue.detect_finger_by_hsv(frameunblurred0,lower_black, upper_black)

    cv2.imshow("frame", frameunblurred0)
    cv2.imshow("mask", mask)

    # cv2.imshow('frame0',frame0)
    # cv2.imshow('frame1',frame1)
    #
    #
    #
    #
    # cv2.imshow('mask0',mask0)
    # cv2.imshow('mask1', mask1)
    k = cv2.waitKey(1) & 0xFF

    if k == ord('p'):
        break
    # print(hierarchy)

cv2.destroyAllWindows()