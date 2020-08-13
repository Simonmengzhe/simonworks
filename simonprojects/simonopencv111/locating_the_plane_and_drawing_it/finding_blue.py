import cv2

import cv2
import numpy as np


def detect_finger_by_hsv(frame, l_hsv, u_hsv):

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #

    l_b = np.array([l_hsv[0], l_hsv[1], l_hsv[2]])
    u_b = np.array([u_hsv[0], u_hsv[1], u_hsv[2]])

    mask = cv2.inRange(frame, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow("frame", frame)
    # cv2.imshow("mask", mask)
    # cv2.imshow("res", res)
    return res, mask


def detect_finger_by_contours(frame):

    # imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(imgray, (5, 5), 0)  # blur
    # blur = cv2.bilateralFilter(frame, 9, 75, 75)
    # _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
    # trans = cv2.dilate(thresh, None, iterations=2)
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    x_list = []
    y_list = []
    w_list = []
    h_list = []
    points = np.array([])
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        x_list.append(x)
        y_list.append(y)
        w_list.append(w)
        h_list.append(h)
        if cv2.contourArea(contour) < 400:
            pass
            # cv2.drawContours(frame, contours, -1, (255, 255, 0), 3)
            # cv2.circle(frame, (int(x+w/2), int(y+h/2)), 20, (255, 34, 34), -1)
    if len(contours) == 0:
        cv2.putText(frame, 'No Finger Detected - hold on', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1)
    cv2.imshow('feed2', frame)
    # x_list = np.array([x_list])
    # y_list = np.array([y_list])
    # location = (x_list, y_list)
    points = [(x, y)for x, y in zip(x_list, y_list)]
    points.sort()
    return points

