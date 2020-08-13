
import cv2
import numpy as np
from locating_the_plane_and_drawing_it import finding_blue

#target color from bgr to hsv
color = np.uint8([[[255 ,0  ,0 ]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print(hsv_color)

#import videocapture
cap0 = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture(0)

#creating trackbars
def nothing(x):
    pass
cv2.namedWindow("Parameters", cv2.WINDOW_NORMAL)
cv2.createTrackbar("L_A", "Parameters", 0, 255, nothing)
cv2.createTrackbar("L_B", "Parameters", 0, 255, nothing)
cv2.createTrackbar("L_C", "Parameters", 0, 255, nothing)
cv2.createTrackbar("H_A", "Parameters", 255, 255, nothing)
cv2.createTrackbar("H_B", "Parameters", 255, 255, nothing)
cv2.createTrackbar("H_C", "Parameters", 255, 255, nothing)
cv2.createTrackbar("SEP", "Parameters", 220, 255, nothing)
cv2.createTrackbar("Focal Length", "Parameters", 12, 150, nothing)

cv2.createTrackbar("minarea", "Parameters", 5000, 30000, nothing)
cv2.createTrackbar("kernel", "Parameters", 1, 19, nothing)
cv2.createTrackbar("OKN", "Parameters", 1, 19, nothing)
#infinite loop
while(1):

    # Take each frame and blur
    _,frameunblurred0 = cap0.read()
    frameunblurred0 = frameunblurred0[60:400,:,:]
    kn =cv2.getTrackbarPos("kernel", "Parameters")*2+1
    frame0 =  cv2.GaussianBlur(frameunblurred0, (kn, kn), 0)
    frame0 = cv2.medianBlur(frameunblurred0, kn, 0)
    # frame0 = frameunblurred0
    bgr0 = frame0
    # bgr0 = cv2.morphologyEx(bgr0, cv2.MORPH_OPEN, (okn, okn))
    # Convert BGR to HSV
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # bgr = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    # 11111111111111111111Take each frame and blur
    _, frameunblurred1 = cap1.read()
    frameunblurred1 = frameunblurred1[60:400, :, :]
    kn = cv2.getTrackbarPos("kernel", "Parameters")*2+1
    frame1= cv2.medianBlur(frameunblurred1, kn, 0)
    # frame1 = frameunblurred1
    bgr1 = frame1
    # bgr1 = cv2.morphologyEx(bgr1, cv2.MORPH_OPEN, (okn, okn))
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
    okn = cv2.getTrackbarPos("OKN", "Parameters")*2 +1
    lower_black = np.array([la, lb, lc])
    upper_black= np.array([ha, hb, hc])

    # Threshold the HSV image to get only target colors
    mask0 = finding_blue.detect_finger_by_hsv(frame0,lower_black, upper_black)

    #finding centroid of mask 0

    M = cv2.moments(mask0)
    if M["m00"] > 0:
        #drawing centroid
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        pass


    # print(M)

    #11111111Threshold the HSV image to get only target colors
    mask1 = finding_blue.detect_finger_by_hsv(frame1,lower_black, upper_black)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, (okn, okn))
    #finding contours
    contours0, hierarchy = cv2.findContours(mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours0 is not None:


        #draw contours approximated as polygons and above minimum area
        for cnt in contours0:

            hull0 = cv2.convexHull(cnt, returnPoints=True)

            cnt = cv2.approxPolyDP(hull0, 0.05*cv2.arcLength(cnt, True), True)
            area = cv2.contourArea(cnt)
            # print(area)
            minarea = cv2.getTrackbarPos("minarea", "Parameters")
            if area > minarea:
                cnt0 = cnt[0]
                leftmost0 = tuple(cnt0[cnt0[:, :, 0].argmin()][0])
                rightmost0 = tuple(cnt0[cnt0[:, :, 0].argmax()][0])
                topmost0 = tuple(cnt0[cnt0[:, :, 1].argmin()][0])
                bottommost0 = tuple(cnt0[cnt0[:, :, 1].argmax()][0])
                cv2.drawContours(frame0, [cnt], 0, (0, 200, 200), 5)
                # cnt0= [approx0][0]
            else:
                pass

            #111111111 finding contours
        contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # draw contours approximated as polygons and above minimum area



        if contours1 is not None:

            for cnt in contours1:

                hull1 = cv2.convexHull(cnt, returnPoints=True)

                cnt = cv2.approxPolyDP(hull1, 0.001 * cv2.arcLength(cnt, True), True)
                area = cv2.contourArea(cnt)
                cnt1 = cnt[0]
                # print(area)
                minarea = cv2.getTrackbarPos("minarea", "Parameters")
                if area > minarea:
                    cv2.drawContours(frame1, [cnt], 0, (0, 200, 200), 5)
                    leftmost1 = tuple(cnt1[cnt1[:, :, 0].argmin()][0])
                    rightmost1 = tuple(cnt1[cnt1[:, :, 0].argmax()][0])
                    topmost1 = tuple(cnt1[cnt1[:, :, 1].argmin()][0])
                    bottommost1 = tuple(cnt1[cnt1[:, :, 1].argmax()][0])


                else:
                    pass
        else:
            pass

        cnt1 = contours1[0]

        # cnt1 = sorted(cnt1, key=cv2.contourArea, reverse=True)[:5]
        # print("sorted", cnt1)
        # cnt1 = cnt1[0]
        # cnt0 = contours0[0]
        # print("sorted with position 0", cnt1)
        # print("not sorted", cnt0)
        # print("len of contour: ",[len(x) for x in contours1])
        #drawing hull
        # hull0  = cv2.convexHull(cnt0, returnPoints=True)
        # hull1 = cv2.convexHull(cnt1, returnPoints=True)
        # finding 4 corners

        # 1111finding 4 corners




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
        # Draw a circle with blue line borders of thickness of 2 px
        frame0 = cv2.circle(frame0, leftmost0, radius, color, thickness)
        frame0 = cv2.circle(frame0, rightmost0, radius, color, thickness)
        frame0 = cv2.circle(frame0, topmost0, radius, color, thickness)
        frame0 = cv2.circle(frame0, bottommost0, radius, color, thickness)

        # Using cv2.circle() method
        # Draw a circle with blue line borders of thickness of 2 px
        frame1 = cv2.circle(frame1, leftmost1, radius, color, thickness)
        frame1 = cv2.circle(frame1, rightmost1, radius, color, thickness)
        frame1 = cv2.circle(frame1, topmost1, radius, color, thickness)
        frame1 = cv2.circle(frame1, bottommost1, radius, color, thickness)



        f = cv2.getTrackbarPos("Focal Length", "Parameters")

        #get separation between cameras

        sep = cv2.getTrackbarPos("SEP", "Parameters")


        def get3d(v1, v2, focalength, seperation):
            l0 = np.hstack((v1, focalength))
            l1 = np.hstack((v2, focalength))
            k_l = sep / (l1[0] - l0[0])
            l_3d = k_l * l0

            return l_3d

        left = get3d(leftmost0, leftmost1, f, sep)
        right = get3d(rightmost0, rightmost1, f, sep)
        top = get3d(topmost0, topmost1, f, sep)
        bot = get3d(bottommost0, bottommost1, f, sep)

        def getnormal3points(a, b, c):
            v1 = b-a
            v2 = c-a
            normal = np.cross(v1, v2)

            return normal

        normal = getnormal3points(top, left, right)





        # diagnol_a = l_3d - r_3d
        # diagnol_b = t_3d - b_3d
        #
        # midpoint = np.around(0.5 * (l0 + b0))
        # mp_2d = diagnol_a[0:2]
        # mp_2d = mp_2d.astype(int)
        # mp_2d = (rightmost0 + mp_2d)

        # n = np.cross(diagnol_b, diagnol_a)
        n_2d = np.around(normal[0:2])
        n_img = (cX, cY) + n_2d
        n_img = n_img.astype(int)
        # print(n_img)

        print(normal)

        red = (0, 0, 255)

        frame0 = cv2.line(frame0, (cX, cY), tuple(n_img), red, thickness=5)
        # frame0 = cv2.line(frame0, leftmost0, rightmost0, red, thickness=5)
        # frame0 = cv2.line(frame0, topmost0, bottommost0, red, thickness=5)

        cv2.circle(frame0, (cX, cY), 5, (255, 255, 255), -1)

        cv2.putText(frame0 , "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        print(leftmost0)
    else:
        pass

    cv2.imshow('frame0',frame0)
    cv2.imshow('frame1',frame1)




    cv2.imshow('mask0',mask0)
    cv2.imshow('mask1', mask1)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('p'):
        break
    # print(hierarchy)

cv2.destroyAllWindows()