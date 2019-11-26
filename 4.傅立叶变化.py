'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-11-25 10:43
@Software: PyCharm
@File    : 4.傅立叶变化.py
'''
from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:30:10 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('img/2.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# 这里构建振幅图的公式没学过
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
rows, cols = img.shape
crow,ccol = rows/2 , cols/2
print(fshift[1:4,1:4])
print(fshift[crow-30:crow+30, ccol-30:ccol+30])
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()