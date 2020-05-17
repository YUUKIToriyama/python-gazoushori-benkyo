#!/usr/bin/python3

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/rose.png")

_, threshold_img = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)
threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)

plt.imshow(threshold_img)
plt.show()
