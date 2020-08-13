import cv2
import numpy as np
from locating_the_plane_and_drawing_it import finding_blue
from locating_the_plane_and_drawing_it import trackbar_creater

# target color from bgr to hsv

color = np.uint8([[[0, 0, 255]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
print(hsv_color)
fivelocations = np.zeros([10, 2])
# import videocapture
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

# creating trackbars
trackbar_creater.create_track_bar()

# infinite loop
while (1):
    framecount = 0


    # Take each frame and blur

    def getbgrdata(camerano):
        _, frameunblurred = camerano.read()
        frameunblurred = frameunblurred[100:360, 150:-150, :]
        kn = cv2.getTrackbarPos("kernel", "Parameters") * 2 + 1
        frame0 = cv2.GaussianBlur(frameunblurred, (kn, kn), 0)
        frame0 = cv2.medianBlur(frameunblurred, kn, 0)
        # frame0 = frameunblurred0
        output = frame0

        return output, frameunblurred


    frame0, frameunblurred0 = getbgrdata(cap0)
    # Convert BGR to HSV
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # bgr = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    # 11111111111111111111Take each frame and blur
    frame1, frameunblurred1 = getbgrdata(cap1)
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

    lower_black = np.array([la, lb, lc])
    upper_black = np.array([ha, hb, hc])

    # Threshold the HSV image to get only target colors
    mask0 = finding_blue.detect_finger_by_hsv(frameunblurred0, lower_black, upper_black)

    # finding centroid of mask 0
    cX = 100
    cY = 100
    M = cv2.moments(mask0)
    if M["m00"] > 0:
        # drawing centroid
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        pass

    # print(M)

    # 11111111Threshold the HSV image to get only target colors
    mask1 = finding_blue.detect_finger_by_hsv(frameunblurred1, lower_black, upper_black)

    # finding contours
    contours0, hierarchy = cv2.findContours(mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours0 is not None:

        # draw contours approximated as polygons and above minimum area
        for cnt in contours0:

            hull0 = cv2.convexHull(cnt, returnPoints=True)

            cnt = cv2.approxPolyDP(hull0, 0.05 * cv2.arcLength(cnt, True), True)
            area = cv2.contourArea(cnt)
            # print(area)
            minarea = cv2.getTrackbarPos("minarea", "Parameters")
            if area > minarea:

                cv2.drawContours(frame0, [cnt], 0, (0, 200, 200), 5)
                # cnt0= [approx0][0]
            else:
                pass

            # 111111111 finding contours
        contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # draw contours approximated as polygons and above minimum area

        if contours1 is not None:

            for cnt in contours1:

                hull1 = cv2.convexHull(cnt, returnPoints=True)

                cnt = cv2.approxPolyDP(hull1, 0.001 * cv2.arcLength(cnt, True), True)
                area = cv2.contourArea(cnt)
                # print(area)
                minarea = cv2.getTrackbarPos("minarea", "Parameters")
                if area > minarea:
                    cv2.drawContours(frame1, [cnt], 0, (0, 200, 200), 5)
                    # cnt1 = [approx1][0]
                else:
                    pass
        else:
            pass


        mylist = finding_blue.detect_finger_by_contours()
        # cnt1 = contours1[0]
        # cnt0 = contours0[0]

        # grey0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
        # corners0 = cv2.goodFeaturesToTrack(grey0, 4, 0.01, 20)
        # corners0 = np.int0(corners0)
        # for i in corners0:
        #     x, y = i.ravel()
        #     cv2.circle(frame0, (x, y), 3, 255, -1)
        #
        # grey1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        # corners1 = cv2.goodFeaturesToTrack(grey1, 4, 0.01, 20)
        # corners1 = np.int0(corners1)
        # for i in corners1:
        #     x, y = i.ravel()
        #     cv2.circle(frame1, (x, y), 3, 255, -1)
        #
        # # corners0 = sorted(contours0, key=lambda x: x[0])
        # # corners1 = sorted(contours1, key=lambda x: x[0])
        #
        # leftmost0 = (corners0[0])[0]
        # rightmost0 = (corners0[1])[0]
        # topmost0 = (corners0[2])[0]
        # bottommost0 = (corners0[3])[0]
        #
        # corners0 = np.array([leftmost0, rightmost0, topmost0, bottommost0])
        # corners0 = sorted(corners0, key=lambda x: x[0])
        # leftmost0 = corners0[0]
        # rightmost0 = corners0[1]
        # topmost0 = corners0[2]
        # bottommost0 = corners0[3]
        #
        # leftmost1 = (corners1[0])[0]
        # rightmost1 = (corners1[1])[0]
        # topmost1 = (corners1[2])[0]
        # bottommost1 = (corners1[3])[0]
        # corners1 = np.array([leftmost1, rightmost1, topmost1, bottommost1])
        # corners1 = sorted(corners1, key=lambda x: x[0])
        # leftmost1 = corners1[0]
        # rightmost1 = corners1[1]
        # topmost1 = corners1[2]
        # bottommost1 = corners1[3]

        if framecount > 12:

            rightmost0 = stablize(rightmost0, fivelocations)
            leftmost0 = stablize(leftmost0, fivelocations)
            topmost0 = stablize(topmost0, fivelocations)
            bottommost0 = stablize(bottommost0, fivelocations)

            rightmost1 = stablize(rightmost1, fivelocations)
            leftmost1 = stablize(leftmost1, fivelocations)
            topmost1 = stablize(topmost1, fivelocations)
            bottommost1 = stablize(bottommost1, fivelocations)

        else:
            pass

        f = cv2.getTrackbarPos("Focal Length", "Parameters")

        # get separation between cameras

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


        # stablizing

        def stablize(a, P):

            fivelocations = np.vstack((fivelocations, a))
            fivelocations = fivelocations[1:, :]

            pos3d = np.mean(fivelocations, axis=0)
            return pos3d


        def getnormal3points(a, b, c):
            v1 = b - a
            v2 = c - a
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

        if normal[1] > 0:
            normal = -1 * normal

        else:
            pass

        n_2d = np.around(normal[0:2])
        n_img = (cX, cY) + n_2d
        start = (cX, cY) - n_2d
        end = n_img.astype(int)
        start = start.astype(int)

        # print(n_img)

        print("this is normal", normal)

        red = (0, 0, 255)

        frame0 = cv2.line(frame0, tuple(start), tuple(end), red, thickness=5)
        # frame0 = cv2.line(frame0, leftmost0, rightmost0, red, thickness=5)
        # frame0 = cv2.line(frame0, topmost0, bottommost0, red, thickness=5)

        cv2.circle(frame0, (cX, cY), 5, (255, 255, 255), -1)

        cv2.putText(frame0, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        framecount += 1


    else:
        print("no contours detected")
        pass
    cv2.circle(frame0, (200, 250), 10, 255, -1)

    cv2.circle(frame0, (190, 250), 10, 255, -1)
    cv2.imshow('frame0', frame0)
    cv2.imshow('frame1', frame1)
    cv2.imshow('grey0', grey0)
    cv2.imshow('mask0', mask0)
    cv2.imshow('mask1', mask1)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('p'):
        break
    # print(hierarchy)

cv2.destroyAllWindows()

