import cv2
import numpy as np
from math import *
def rotate(img,box):
    img = cv2.drawContours(img, [box], 0, color=(255, 0, 0), thickness=4)
    cv2.imwrite('4检测到目标.jpg', img)
    t = list(box)
    pt1, pt2, pt3, pt4=list(t[0]),list(t[1]),list(t[2]),list(t[3])
    withRect = sqrt((pt4[0] - pt1[0]) ** 2 + (pt4[1] - pt1[1]) ** 2)  # 矩形框的宽度
    heightRect = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) **2)
    angle = acos((pt4[0] - pt1[0]) / withRect) * (180 / pi)  # 矩形框旋转角度
    if pt4[1]>pt1[1]:
        print("顺时针旋转")
    else:
        print("逆时针旋转")
        angle=-angle

    height = img.shape[0]  # 原始图像高度
    width = img.shape[1]   # 原始图像宽度
    rotateMat = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)  # 按angle角度旋转图像
    heightNew = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))
    widthNew = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))

    rotateMat[0, 2] += (widthNew - width) / 2
    rotateMat[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, rotateMat, (widthNew, heightNew), borderValue=(255, 255, 255))
    cv2.imwrite('5目标转正.jpg',  imgRotation)

    # 旋转后图像的四点坐标
    [[pt1[0]], [pt1[1]]] = np.dot(rotateMat, np.array([[pt1[0]], [pt1[1]], [1]]))
    [[pt3[0]], [pt3[1]]] = np.dot(rotateMat, np.array([[pt3[0]], [pt3[1]], [1]]))
    [[pt2[0]], [pt2[1]]] = np.dot(rotateMat, np.array([[pt2[0]], [pt2[1]], [1]]))
    [[pt4[0]], [pt4[1]]] = np.dot(rotateMat, np.array([[pt4[0]], [pt4[1]], [1]]))

    # 处理反转的情况
    if pt2[1]>pt4[1]:
        pt2[1],pt4[1]=pt4[1],pt2[1]
    if pt1[0]>pt3[0]:
        pt1[0],pt3[0]=pt3[0],pt1[0]

    imgOut = imgRotation[int(pt2[1]):int(pt4[1]), int(pt1[0]):int(pt3[0])]
    cv2.imwrite("imgOut.jpg", imgOut)  # 裁减得到的旋转矩形框
    return imgRotation  # rotated image

img_0=cv2.imread('img/1.jpg',0)
gray=img_0.copy()
cv2.imwrite("0原图.jpg",gray)
# 高斯平滑
gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("1高斯滤波后.jpg",gaussian)

# 二值化
ret2, binary = cv2.threshold(gray,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("2二值化后.jpg",binary)
kernel = np.ones((5,5), np.uint8)
# 膨胀一次，让轮廓突出
dilation = cv2.dilate(binary, kernel, iterations=1)
# 腐蚀一次，去掉细节
erosion = cv2.erode(dilation, kernel, iterations=1)
# 再次膨胀，让轮廓明显一些
dilation2 = cv2.dilate(erosion, kernel, iterations=1)
cv2.imwrite("3形态学处理后.jpg",dilation2)

region = []
angel=[]
c,contours, hierarchy= cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if (area < 5000 or area>300000):
        continue
    rect = cv2.minAreaRect(cnt)
    print("rect is: %s area is :%s"%(rect,area))
    # box是四个点的坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    height = sqrt((box[3][0] - box[0][0]) ** 2 + (box[3][1] - box[0][1]) ** 2)
    width = sqrt((box[0][0] - box[1][0]) ** 2 + (box[0][1] - box[1][1]) ** 2)
    print("height=%s,width=%s"%(height,width))
    ratio = float(width) / float(height)
    print(ratio)
    region.append(box)

for box in region:
    rotate(img_0,box)





# print(img.size)
# print(img.shape)
# w=img.shape[0]
# h=img.shape[1]
# for i in range(w):
#     for j in range(h):
#         if img[i][j]<100:
#             img2[i][j]=0
# cv2.imwrite("t.jpg",img2)