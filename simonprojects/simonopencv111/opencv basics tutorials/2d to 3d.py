import cv2
import numpy as np

#calibrated parameters
focal_length = 35
f = focal_length
deviation = 8
p_camera1 = np.array[0, 0, 0]
p_camera2 = np.array[deviation , 0, 0]
#data input as position on frame r1 and r2 from camera1 and camera2 respectively

#initial default position of A
p_a = np.zeros((1,3))
print(p_a)
#position of a on both image screens
a1 = np.array[x1, y1, z0]
a2 = np.array[x2, y2, z0]

k = deviation/()