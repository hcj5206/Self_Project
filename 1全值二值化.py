'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-11-23 18:22
@Software: PyCharm
@File    : 1全值二值化.py
'''
from __future__ import print_function
import cv2
from matplotlib import pyplot as plt
'''
　cv2.THRESH_BINARY：大于阈值的部分像素值变为maxval，其他变为0 
　　　　cv2.THRESH_BINARY_INV：大于阈值的部分变为0，其他部分变为最大值 
　　　　cv2.THRESH_TRUNC：大于阈值的部分变为阈值，其余部分不变 
　　　　cv2.THRESH_TOZERO：大于阈值的部分不变，其余部分变为0 
　　　　cv2.THRESH_TOZERO_INV：大于阈值的部分变为0，其余部分不变
'''
img_0=cv2.imread('img/1.jpg',0)
img=img_0.copy()
cv2.imwrite("0原图.jpg",img)
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3=cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4=cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5=cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i + 1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()