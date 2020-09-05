# https://blog.csdn.net/weixin_41869763/article/details/104067851
# coding:UTF-8
# v1--读取与显示图像
import cv2
import numpy as np

img_bgr = cv2.imread('D:\code\opencv_learning\opencv_learning\last\DATA1.jpg',0)   #读取图像

cv2.imshow('原始图像', img_bgr)            #显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()
