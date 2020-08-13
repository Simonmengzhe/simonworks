import cv2
import numpy as np

img = cv2.imread('4circlesonpaper.png',0)



leftmost0 = (300,300)
rightmost0 =(700,700)
topmost0 = (500,0)
bottommost0 =(500,1100)
# 1111finding 4 corners
leftmost1 =(350,300)
rightmost1 =(760 ,700)
topmost1 =(560, 0)
bottommost1 =(5300, 1100)


focal_length = 10
f = focal_length

l0 = np.hstack((leftmost0, f))
l1 = np.hstack((leftmost1, f))
k_l = f / (l1[0] - l0[0])
l_3d = k_l * l1

r0 = np.hstack((rightmost0, f))
r1 = np.hstack((rightmost1, f))
k_r = f / (r1[0] - r0[0])
r_3d = k_r * r1

t0 = np.hstack((topmost0, f))
t1 = np.hstack((topmost1, f))
k_t = f / (t1[0] - t0[0])
t_3d = k_t * t1

b0 = np.hstack((bottommost0, f))
b1 = np.hstack((bottommost1, f))
k_b = f / (b1[0] - b0[0])
b_3d = k_b * b1

diagnol_a = l_3d - r_3d
diagnol_b = t_3d - b_3d

midpoint = np.around(0.5*(l0 + b0))
mp_2d = diagnol_a[0:2]/k_l
mp_2d = mp_2d.astype(int)
mp_2d = (rightmost0 + mp_2d)

n = np.cross(diagnol_a, diagnol_b)
n_2d = np.around(n[0:2])
n_img = mp_2d + n_2d
n_img = n_img.astype(int)
print(n_img)
print(n_2d)
print(n)


red = (0, 0, 255)

cv2.line(img, tuple(mp_2d), tuple(n_img), red, thickness=5)
cv2.line(img, leftmost0, rightmost0, red, thickness=5)
cv2.line(img, topmost0, bottommost0, red, thickness=5)


cv2.circle(img,tuple(mp_2d), 23, red, -1)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

