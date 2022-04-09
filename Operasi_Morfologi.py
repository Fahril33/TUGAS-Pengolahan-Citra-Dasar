
import cv2 as cv2
import numpy as np
# import matplotlib.pyplot as plt

# Original
img = cv2.imread("letter_f.jpg")
imo = cv2.resize(img, (560, 340))
cv2.imshow("Original", imo)
cv2.waitKey(0)

kernel= np.ones((5,5),np.uint8)

# Erosion
erosion = cv2.erode(img,kernel,iterations = 1)
ime = cv2.resize(img, (560, 340))
cv2.imshow("Erosion", ime)
cv2.waitKey(0)

# Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)
imd = cv2.resize(img, (560, 340))
cv2.imshow("Dilasi", imd)
cv2.waitKey(0)

# Opening
kernel1 = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel1)
imop = cv2.resize(img, (560, 340))
cv2.imshow('opening', imop)
cv2.waitKey(0)

# Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
imc = cv2.resize(img, (560, 340))
cv2.imshow("Closing", imc)
cv2.waitKey(0)

# Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
imgr = cv2.resize(img, (560, 340))
cv2.imshow("Gradient", imgr)
cv2.waitKey(0)
