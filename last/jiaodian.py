#! /usr/bin/env python
#-- coding:UTF-8 --
import cv2
import numpy as np
from matplotlib import pyplot as plt

title1 = 'input'
title2 = 'output'
img = cv2.imread('D:\code\opencv_learning\opencv_learning\last\DATA1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
for i in corners:
    print (i)
    #将双括号数组转化为一维
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imshow('1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()