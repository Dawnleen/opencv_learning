#! /usr/bin/env python
#-- coding:UTF-8 --
import cv2
import numpy as np
from matplotlib import pyplot as plt

#要匹配的物体
img1 = cv2.imread(r'D:\code\opencv_learning\opencv_learning\last\DATA1.png')
#待匹配的景物图
img2 = cv2.imread(r'D:\code\opencv_learning\opencv_learning\last\2_2.png')

orb = cv2.ORB_create()
#寻找关键点并计算描述符
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#创建BF匹配器
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
#匹配描述符
matches = bf.match(des1,des2)
#按照距离进行匹配
matches = sorted(matches,key=lambda x:x.distance)
#绘制最佳匹配点
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)

# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()