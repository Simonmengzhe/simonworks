import cv2
import numpy as np

#target color from bgr to hsv
color = np.uint8([[[0  ,0  ,255 ]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print(hsv_color)

#import videocapture
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

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
cv2.createTrackbar("SEP", "Parameters", 7, 150, nothing)
cv2.createTrackbar("Focal Length", "Parameters", 7, 150, nothing)

cv2.createTrackbar("minarea", "Parameters", 5000, 30000, nothing)
cv2.createTrackbar("kernel", "Parameters", 1, 19, nothing)
cv2.createTrackbar("MINDIS", "Parameters", 50, 500, nothing)
cv2.createTrackbar("QUALITY", "Parameters", 1, 99, nothing)

#infinite loop
while(1):

    # Take each frame and blur
    _,frameunblurred0 = cap0.read()
    frameunblurred0 = frameunblurred0[60:400,:,:]
    kn =cv2.getTrackbarPos("kernel", "Parameters")*2+1
    frame0 =  cv2.GaussianBlur(frameunblurred0, (kn, kn), 0)
    frame0 = frameunblurred0
    bgr0 = frame0
    # Convert BGR to HSV
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # bgr = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    # 11111111111111111111Take each frame and blur
    _, frameunblurred1 = cap1.read()
    frameunblurred1 = frameunblurred1[60:400, :, :]
    kn = cv2.getTrackbarPos("kernel", "Parameters")*2+1
    frame1= cv2.GaussianBlur(frameunblurred1, (kn, kn), 0)
    frame1 = frameunblurred1
    bgr1 = frame1
    # Convert BGR to HSV
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # bgr = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)






    # define range of target color in HSV from trackbars
    la = cv2.getTrackbarPos("L_A", "Parameters")
    lb = cv2.getTrackbarPos("L_B", "Parameters")
    lc = cv2.getTrackbarPos("L_C", "Parameters")
    ha = cv2.getTrackbarPos("H_A", "Parameters")
    hb = cv2.getTrackbarPos("H_B", "Parameters")
    hc = cv2.getTrackbarPos("H_C", "Parameters")

    mindis = cv2.getTrackbarPos("MINDIS", "Parameters")
    qlty = cv2.getTrackbarPos("QUALITY", "Parameters") / 100

    lower_black = np.array([la, lb, lc])
    upper_black= np.array([ha, hb, hc])

    # Threshold the HSV image to get only target colors
    mask0 = cv2.inRange(bgr0, lower_black, upper_black)
    mask0 = cv2.GaussianBlur(mask0,(kn, kn), 0)

    #finding centroid of mask 0

    M = cv2.moments(mask0)

    #drawing centroid
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])



    # print(M)
    #11111111Threshold the HSV image to get only target colors
    mask1 = cv2.inRange(bgr1, lower_black, upper_black)
    mask1 = cv2.GaussianBlur(mask1, (kn, kn), 0)

    #finding contours
    contours0, hierarchy = cv2.findContours(mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #draw contours approximated as polygons and above minimum area
    for cnt in contours0:

        hull0 = cv2.convexHull(cnt, returnPoints=True)
        area = cv2.contourArea(hull0)
        approx0 = cv2.approxPolyDP(hull0, 0.05*cv2.arcLength(cnt, True), True)
        # print(area)吗
        minarea = cv2.getTrackbarPos("minarea", "Parameters")
        if area > minarea:

            cv2 .drawContours(frame0, [approx0], 0, (0, 200, 200), 5)

        else:
            pass

        #111111111 finding contours
    contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw contours approximated as polygons and above minimum area
    for cnt in contours1:

        hull1 = cv2.convexHull(cnt, returnPoints=True)
        area = cv2.contourArea(hull1)
        approx1 = cv2.approxPolyDP(hull1, 0.001 * cv2.arcLength(cnt, True), True)
        # print(area)
        minarea = cv2.getTrackbarPos("minarea", "Parameters")
        if area > minarea:
            cv2.drawContours(frame1, [approx1], 0, (0, 200, 200), 5)

        else:
            pass

    cnt0 = contours0[0]
    cnt1 = contours1[0]

    blacknwhite0 = np.float32(mask0)

    corners0 = cv2.goodFeaturesToTrack(blacknwhite0, 4, qlty, mindis)

    if corners0 is not None:

        corners0 = np.int0(corners0)

        for cnr in corners0:
            x, y = cnr.ravel()
            cv2.circle(frame0, (x, y), 3, 255, -1)
            # print(corners0[0])
    else:
        continue

    blacknwhite1 = np.float32(mask1)

    corners1 = cv2.goodFeaturesToTrack(blacknwhite1, 4, qlty, mindis)

    if corners1 is not None:

        corners1 = np.int0(corners1)

        for cnr in corners1:
            x, y = cnr.ravel()
            cv2.circle(frame1, (x, y), 3, 255, -1)
            # print(corners1[0])
    else:
        continuep

    #drawing hull
    # hull0  = cv2.convexHull(cnt0, returnPoints=True)
    # hull1 = cv2.convexHull(cnt1, returnPoints=True)
    # finding 4 corners
    leftmost0 = tuple(corners0[0, 0])
    rightmost0 = tuple(corners0[1, 0])
    topmost0 = tuple(corners0[2, 0])
    bottommost0 = tuple(corners0[3, 0])
    # 1111finding 4 corners
    leftmost1 = tuple(corners1[0, 0])
    rightmost1 = tuple(corners1[1, 0])
    topmost1 = tuple(corners1[2, 0])
    bottommost1 = tuple(corners1[3, 0])

    #drawing hull
    # hull0  = cv2.convexHull(cnt0, returnPoints=True)
    # hull1 = cv2.convexHull(cnt1, returnPoints=True)
    # # finding 4 corners
    # leftmost0 = tuple(cnt0[cnt0[:, :, 0].argmin()][0])
    # rightmost0 = tuple(cnt0[cnt0[:, :, 0].argmax()][0])
    # topmost0 = tuple(cnt0[cnt0[:, :, 1].argmin()][0])
    # bottommost0 = tuple(cnt0[cnt0[:, :, 1].argmax()][0])
    # # 1111finding 4 corners
    # leftmost1 = tuple(cnt1[cnt1[:, :, 0].argmin()][0])
    # rightmost1 = tuple(cnt1[cnt1[:, :, 0].argmax()][0])
    # topmost1 = tuple(cnt1[cnt1[:, :, 1].argmin()][0])
    # bottommost1 = tuple(cnt1[cnt1[:, :, 1].argmax()][0])




    # print(leftmost0)


    # drawing contours
    # cv2.drawContours(frame0, [hull0], 0, (0, 0, 255), 5)
    #
    # cv2.drawContours(frame1, [hull1], 0, (0, 0, 255), 5)

    # Radius of circle
    radius = 5

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = -1

    # Using cv2.circle() method
    # # Draw a circle with blue line borders of thickness of 2 px
    # frame0 = cv2.circle(frame0, leftmost0, radius, color, thickness)
    # frame0 = cv2.circle(frame0, rightmost0, radius, color, thickness)
    # frame0 = cv2.circle(frame0, topmost0, radius, color, thickness)
    # frame0 = cv2.circle(frame0, bottommost0, radius, color, thickness)
    #
    # # Using cv2.circle() method
    # # Draw a circle with blue line borders of thickness of 2 px
    # frame1 = cv2.circle(frame1, leftmost1, radius, color, thickness)
    # frame1 = cv2.circle(frame1, rightmost1, radius, color, thickness)
    # frame1 = cv2.circle(frame1, topmost1, radius, color, thickness)
    # frame1 = cv2.circle(frame1, bottommost1, radius, color, thickness)


    focal_length = 10
    f = cv2.getTrackbarPos("Focal Length", "Parameters")

    #get separation between cameras

    sep = cv2.getTrackbarPos("SEP", "Parameters")

    l0 = np.hstack((leftmost0, f))
    l1 = np.hstack((leftmost1, f))
    k_l = sep / (l1[0] - l0[0])
    l_3d = k_l * l1

    r0 = np.hstack((rightmost0, f))
    r1 = np.hstack((rightmost1, f))
    k_r = sep / (r1[0] - r0[0])
    r_3d = k_r * r1

    t0 = np.hstack((topmost0, f))
    t1 = np.hstack((topmost1, f))
    k_t = sep / (t1[0] - t0[0])
    t_3d = k_t * t1

    b0 = np.hstack((bottommost0, f))
    b1 = np.hstack((bottommost1, f))
    k_b = sep / (b1[0] - b0[0])
    b_3d = k_b * b1

    diagnol_a = l_3d - r_3d
    diagnol_b = t_3d - b_3d

    midpoint = np.around(0.5 * (l0 + b0))
    mp_2d = diagnol_a[0:2]
    mp_2d = mp_2d.astype(int)
    mp_2d = (rightmost0 + mp_2d)

    n = np.cross(diagnol_b, diagnol_a)
    n_2d = np.around(n[0:2])
    n_img = (cX, cY) + n_2d
    n_img = n_img.astype(int)
    # print(n_img)
    print(diagnol_a, diagnol_b)
    print(n)

    red = (0, 0, 255)

    frame0 = cv2.line(frame0, (cX, cY), tuple(n_img), red, thickness=5)
    # frame0 = cv2.line(frame0, leftmost0, rightmost0, red, thickness=5)
    # frame0 = cv2.line(frame0, topmost0, bottommost0, red, thickness=5)

    cv2.circle(frame0, (cX, cY), 5, (255, 255, 255), -1)

    cv2.putText(frame0 , "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('frame0',frame0)
    cv2.imshow('frame1',frame1)





    cv2.imshow('mask0',mask0)
    cv2.imshow('mask1', mask1)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('p'):
        break
    # print(hierarchy)

cv2.destroyAllWindows()