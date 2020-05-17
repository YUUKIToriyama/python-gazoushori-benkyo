#!/usr/bin/python3

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/rose.png")
img_blur = cv2.GaussianBlur(img, (5,5), 0)

plt.imshow(img_blur)
plt.show()
