# https://segmentfault.com/a/1190000015663722
import cv2
import numpy as np

img = cv2.imread('D:\code\opencv_learning\opencv_learning\last\DATA1.png')
cv2.imshow('src',img)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh =cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
cnt = contours[1]

epsilon =0.1*cv2.arcLength(cnt, True) 
approx = cv2.approxpolyDP(cnt, epsilon, True)
cv2.polylines(img, [approx], True, (0, 0, 255), 2)
cv2.imshow('show', img)
cv2.waitkey()