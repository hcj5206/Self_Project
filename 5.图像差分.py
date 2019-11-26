'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-11-25 18:39
@Software: PyCharm
@File    : 5.图像差分.py
'''
from __future__ import print_function

import cv2

img_0=cv2.imread('样本集2/img1.jpg',0)
cv2.imwrite("00.jpg",img_0)

img_1=cv2.imread('样本集2/bg.jpg',0)
cv2.imwrite("11.jpg",img_1)


img_0 = cv2.GaussianBlur(img_0, (3, 3), 0)
img_1 = cv2.GaussianBlur(img_1, (3, 3), 0)
img_00=cv2.convertScaleAbs(img_0)
img_01=cv2.convertScaleAbs(img_1)

err1=cv2.convertScaleAbs(img_0 - img_1)
cv2.imwrite("差分1.jpg",err1)

err=cv2.absdiff(img_0,img_1)

cv2.imwrite("差分.jpg",err)
# 二值化
ret2, binary = cv2.threshold(err,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("./二值化后.jpg",binary)