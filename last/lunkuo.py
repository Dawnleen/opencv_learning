#! /usr/bin/env python
#-- coding:UTF-8 --
import cv2
import numpy as np


title1 = 'input'
title2 = 'output'
img = cv2.imread('D:\code\opencv_learning\opencv_learning\last\DATA1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#去除白噪音
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
#确定背景
sure_bg = cv2.dilate(opening,kernel,iterations=3)
#确定前景
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,cv2.THRESH_BINARY)
#边界像素
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
#将背景赋值为1,未知区域赋值为0，确定区域大于1
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
#unknow大小的markers一致
markers[unknown==255] = 0
#用分水岭算法
markers3 = cv2.watershed(img,markers)
img[markers==-1] =[255,0,0]

cv2.imshow('1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()