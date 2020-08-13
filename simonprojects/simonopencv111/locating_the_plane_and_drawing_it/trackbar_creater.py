import cv2
import numpy as np



def create_track_bar():

    def nothing(x):
        pass


    cv2.namedWindow("Parameters", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("L_A", "Parameters", 0, 255, nothing)
    cv2.createTrackbar("L_B", "Parameters", 0, 255, nothing)
    cv2.createTrackbar("L_C", "Parameters", 0, 255, nothing)
    cv2.createTrackbar("H_A", "Parameters", 70, 255, nothing)
    cv2.createTrackbar("H_B", "Parameters", 70, 255, nothing)
    cv2.createTrackbar("H_C", "Parameters", 70, 255, nothing)
    cv2.createTrackbar("SEP", "Parameters", 70, 255, nothing)
    cv2.createTrackbar("Focal Length", "Parameters", 12, 150, nothing)

    cv2.createTrackbar("minarea", "Parameters", 5000, 30000, nothing)
    cv2.createTrackbar("kernel", "Parameters", 1, 19, nothing)


