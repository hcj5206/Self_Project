import cv2
import numpy as np
img = cv2.imread('img/2.jpg', 0)

_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)
cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)