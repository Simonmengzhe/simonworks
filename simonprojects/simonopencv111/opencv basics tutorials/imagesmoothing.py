import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('denoising_example.png')


blur = cv2.blur(img,(3,3))


#blur15 = cv2.blur(img,(15,15))
#blur25 = cv2.blur(img,(15,15))
#blurG5 = cv2.GaussianBlur(img,(5,5),0)
#blurG15 = cv2.GaussianBlur(img,(15,15),0)
#blur = cv2.GaussianBlur(img,(33,3),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred5')
plt.xticks([]), plt.yticks([])
#plt.subplot(123),plt.imshow(blur15),plt.title('Blurred15')
plt.xticks([]), plt.yticks([])
#plt.subplot(124),plt.imshow(blur25),plt.title('Blurred25')
plt.xticks([]), plt.yticks([])
#plt.subplot(125),plt.imshow(blurG5),plt.title('BlurredG5')
#plt.xticks([]), plt.yticks([])
#plt.subplot(126),plt.imshow(blurG15),plt.title('BlurredG15')
#plt.xticks([]), plt.yticks([])
#plt.subplot(127),plt.imshow(blurG25),plt.title('BlurredG25')
#plt.xticks([]), plt.yticks([])
plt.show()