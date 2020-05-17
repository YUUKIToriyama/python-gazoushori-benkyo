#!/usr/bin/python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/rose.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(gray_img)

plt.imshow(img)
plt.show()
