import cv2
import numpy as np


cap0 = cv2.VideoCapture(0)



#creating trackbars
def nothing(x):
    pass
cv2.namedWindow("Parameters", cv2.WINDOW_NORMAL)
cv2.createTrackbar("L_A", "Parameters", 0, 255, nothing)
cv2.createTrackbar("L_B", "Parameters", 0, 255, nothing)
cv2.createTrackbar("L_C", "Parameters", 0, 255, nothing)
cv2.createTrackbar("H_A", "Parameters", 50, 150, nothing)
cv2.createTrackbar("H_B", "Parameters", 50, 150, nothing)
cv2.createTrackbar("H_C", "Parameters", 50, 150, nothing)
cv2.createTrackbar("MINDIS", "Parameters", 50, 500, nothing)
cv2.createTrackbar("QUALITY", "Parameters", 1, 99, nothing)

cv2.createTrackbar("kernel", "Parameters", 1, 19, nothing)
#infinite loop
while(1):

    # Take each frame and blur
    _,frameunblurred0 = cap0.read()
    frameunblurred0 = frameunblurred0[60:400,:,:]
    kn =cv2.getTrackbarPos("kernel", "Parameters")*2+1
    frame0 =  cv2.GaussianBlur(frameunblurred0, (kn, kn), 0)
    # frame0 = frameunblurred0
    bgr0 = frame0
    # Convert BGR to HSV
    hsv0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2HSV)
    bgr0 = cv2.cvtColor(frame0, cv2.COLOR_HSV2BGR)

    la = cv2.getTrackbarPos("L_A", "Parameters")
    lb = cv2.getTrackbarPos("L_B", "Parameters")
    lc = cv2.getTrackbarPos("L_C", "Parameters")
    ha = cv2.getTrackbarPos("H_A", "Parameters")
    hb = cv2.getTrackbarPos("H_B", "Parameters")
    hc = cv2.getTrackbarPos("H_C", "Parameters")
    mindis = cv2.getTrackbarPos("MINDIS", "Parameters")
    qlty = cv2.getTrackbarPos("QUALITY", "Parameters")/100

    lower_black = np.array([la, lb, lc])
    upper_black = np.array([ha, hb, hc])

    # Threshold the HSV image to get only target colors
    mask0 = cv2.inRange(bgr0, lower_black, upper_black)

    blacknwhite0 = np.float32(mask0)

    corners0 = cv2.goodFeaturesToTrack(blacknwhite0, 4, qlty , mindis)

    if corners0 is not None:

        corners0 = np.int0(corners0)
        print(type(corners0))
        for cnr in corners0:

            x, y = cnr.ravel()
            cv2.circle(frame0, (x, y), 3, 255, -1)
            print(tuple(corners0[0, 0]))

        # continue
        # leftmost = corners0(0)
        #
        # print(leftmost)
    else:
        continue

    cv2.imshow('corners', mask0)
    cv2.imshow('frame0', frame0)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('p'):
        break
    # print(hierarchy)

cv2.destroyAllWindows()