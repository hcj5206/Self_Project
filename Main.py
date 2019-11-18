import cv2
import numpy as np
img=cv2.imread('img/2.jpg',0)
gray=img.copy()
edges = cv2.Canny(gray,80,200)
cv2.imwrite("Canny1.jpg",edges)
# cv2.imwrite("Canny2.jpg",threshimg)

# 高斯平滑
gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
# 中值滤波
median = cv2.medianBlur(gaussian, 5)
cv2.imwrite("t1.jpg",median)

# Sobel算子，X方向求梯度
# 二值化
ret2, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ret, binary = cv2.threshold(median, 100, 255, cv2.THRESH_BINARY)
element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7))
# 膨胀一次，让轮廓突出
dilation = cv2.dilate(binary, element1, iterations=1)
# 腐蚀一次，去掉细节
erosion = cv2.erode(dilation, element1, iterations=1)
# 再次膨胀，让轮廓明显一些
# dilation2 = cv2.dilate(erosion, element2, iterations=1)
cv2.imwrite("t.jpg",binary)
region = []
# 查找轮廓
contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cnt = contours[i]
    # 计算该轮廓的面积
    area = cv2.contourArea(cnt)

    # 面积小的都筛选掉
    if (area < 5000 or area>300000):
        continue

    # 轮廓近似，作用很小
    epsilon = 0.001 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # 找到最小的矩形，该矩形可能有方向
    rect = cv2.minAreaRect(cnt)
    print("rect is: %s area is :%s"%(rect,area))
    # box是四个点的坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 计算高和宽
    height = abs(box[0][1] - box[2][1])
    width = abs(box[0][0] - box[2][0])
    print("height=%s,width=%s"%(height,width))
    # 车牌正常情况下长高比在2.7-5之间
    ratio = float(width) / float(height)
    print(ratio)
    region.append(box)

for box in region:
    img=cv2.drawContours(img, [box], 0, color=(255, 0, 0), thickness=2)

(h, w) = img.shape[:2] #10
center = (w // 2, h // 2) #11
M= cv2.getRotationMatrix2D(center, -23.29456329345703, 1.0) #15

rotated = cv2.warpAffine(img, M, (w, h)) #16

cv2.imwrite('Rotated.jpg', rotated)

# cv2.imshow('number plate', img_plate)
cv2.imwrite('number_plate.jpg', img)

# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.imshow('img', img)

# 带轮廓的图片
cv2.imwrite('contours.png', img)

# print(img.size)
# print(img.shape)
# w=img.shape[0]
# h=img.shape[1]
# for i in range(w):
#     for j in range(h):
#         if img[i][j]<100:
#             img2[i][j]=0
# cv2.imwrite("t.jpg",img2)