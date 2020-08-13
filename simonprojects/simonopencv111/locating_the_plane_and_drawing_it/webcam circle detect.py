import cv2, time 
import numpy as np

circles = np.zeros((3,4))
a = 0
# creating the video
video = cv2.VideoCapture(0)


def nothing(x):
    pass


cv2.namedWindow("Parameters")
cv2.createTrackbar("P1", "Parameters", 10, 70, nothing)
cv2.createTrackbar("P2", "Parameters", 30, 90, nothing)
cv2.createTrackbar("MinR", "Parameters", 5, 40, nothing)
cv2.createTrackbar("MaxR", "Parameters", 40, 200, nothing)

while True:
    a = a + 1

    #create frame
    check, img = video.read()
    bimg = cv2.medianBlur(img, 5)
    dimg = cv2.cvtColor(bimg, cv2.COLOR_BGR2GRAY)
    cimg = cv2.cvtColor(dimg, cv2.COLOR_GRAY2BGR)



    p1 = cv2.getTrackbarPos("P1", "Parameters")
    p2 = cv2.getTrackbarPos("P2", "Parameters")
    minR = cv2.getTrackbarPos("MinR", "Parameters")
    maxR = cv2.getTrackbarPos("MaxR", "Parameters")

    circles = cv2.HoughCircles(dimg, cv2.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    #print(check)

    print(circles[:, 0:1])
    cv2.imshow("WebcamOriginal", img)
    cv2.imshow("WebcamBlurred", bimg)
    cv2.imshow("WebcamC", cimg)
    cv2.imshow("Webcamd", dimg)

    #waitkey
    #cv2.waitKey(0)

    #for playing
    key=cv2.waitKey(1)

    if key == ord('p'):
        break

print(a)
video.release()


cv2.destroyAllWindows()