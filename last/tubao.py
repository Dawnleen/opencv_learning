#! /usr/bin/env python
#-- coding:UTF-8 --
import cv2
import numpy as np

# 新建512*512的空白图片 
img = np.zeros((512,512,3), np.uint8)
# 平面点集
pts = np.array([[200,250], [250,300], [300, 270], [270,200], [120, 240]], np.int32)
pts = pts.reshape((-1,1,2))
# 绘制填充的多边形
cv2.fillPoly(img, [pts], (255,255,255))
# 转至灰度模式
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 图片轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 寻找凸包并绘制凸包（轮廓）
print (contours[0][1])
print (type(contours[0]))
hull = cv2.convexHull(contours[0])
print (hull[1][0])
length = len(hull)
for i in range(len(hull)):
    cv2.line(img, tuple(hull[i][0]), tuple(hull[(i+1)%length][0]), (0,255,0), 2)

# 显示图片
cv2.imshow('line', img)
cv2.waitKey()
