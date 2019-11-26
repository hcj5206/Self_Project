import numpy as np
'''

'''
import cv2
from matplotlib import pyplot as plt

# 读取灰度图
img = cv2.imread("./img/3.jpg", 0)

# 中值滤波，用来平滑图像，去除噪声
img = cv2.medianBlur(img, 5)

# 简单阈值
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 自适应，阈值取相邻区域的平均值
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# 自适应，阈值取值相邻区域的加权和，权重为一个高斯窗口。
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, thresh1, thresh2, thresh3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()