import cv2
img = cv2.imread('img/1.jpg',0)
# # 按照指定的宽度、高度缩放图片
# res = cv2.resize(img, (132, 150))
# # 按照比例缩放，如x,y轴均放大一倍
# print(res.shape)
# cv2.imshow('shrink', res)
# cv2.imshow('shrink1', img)
#
# cv2.waitKey(0)
# 平移图片
import numpy as np
rows, cols = img.shape[:2]
# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 用仿射变换实现平移
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('shift', dst)
cv2.waitKey(0)