'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-11-23 21:12
@Software: PyCharm
@File    : 3、Otus二值化.py


'''
'''
在使用全局阈值时，只能通过不停的尝试来确定一个效果比较好的阈值。如果是一副双峰图像（简单来说双峰图像是指图像直方图中存在两个峰）呢？我们岂不是应该在两个峰之间的峰谷选一个值作为阈值？这就是 Otsu 二值化要做的。简单来说就是对一副双峰图像自动根据其直方图计算出一个阈值。（对于非双峰图像，这种方法得到的结果可能会不理想）。　

函数还是 cv2.threshold()，但是需要多传入一个参数（ flag）： cv2.THRESH_OTSU。这时要把阈值设为 0。然后算法会找到最优阈值，这个最优阈值就是返回值 retVal。如果不使用 Otsu 二值化，返回的retVal 值与设定的阈值相等。

算法分类的原理是让背景和目标之间的类间方差最大，因为背景和目标之间的类间方差越大,说明构成图像的两部分的差别越大,错分的可能性越小。　 
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取灰度图
img = cv2.imread("./img/1.jpg", 0)

# 全局阈值
ret1, th_img1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu’s 二值化
re2, th_img2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Otsu’s 二值化之前先对图像进行高斯滤波处理，平滑图像，去除噪声
# （5,5）为高斯核大小，0为标准差
blur = cv2.GaussianBlur(img, (5, 5), 0)
re3, th_img3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


images = [img, 0, th_img1,
          img, 0, th_img2,
          blur, 0, th_img3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()