'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-11-25 10:06
@Software: PyCharm
@File    : main2.py
'''
from __future__ import print_function
import cv2
import numpy as np
from matplotlib import pyplot as plt
img_0=cv2.imread('img/2.jpg',0)
gray=img_0.copy()
cv2.imwrite("./outimg2/0原图.jpg",gray)
# 高斯滤波
img = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("./outimg2/1高斯滤波后.jpg",img)
edges = cv2.Canny(img,100,200)
cv2.imwrite("./outimg2/2Canny边缘提取.jpg",edges)
kernel = np.ones((5,5), np.uint8)
# 膨胀一次，让轮廓突出
dilation = cv2.dilate(edges, kernel, iterations=1)
cv2.imwrite("./outimg2/3膨胀.jpg",dilation)
# 腐蚀一次，去掉细节
erosion = cv2.erode(dilation, kernel, iterations=1)
cv2.imwrite("./outimg2/4腐蚀.jpg",erosion)
dilation2 = cv2.dilate(erosion, kernel, iterations=1)
cv2.imwrite("./outimg2/5二次膨胀.jpg",dilation2)
region = []
angel=[]
c,contours, hierarchy= cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
