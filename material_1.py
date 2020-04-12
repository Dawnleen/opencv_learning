#coding:utf-8

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"D:/cvpicture/autothers/blackray.jpg",0)
# img = cv.imread(r"D:/cvpicture/camil.jpg",0)

ret,thre1 = cv.threshold(img,120,200,cv.THRESH_BINARY) 
# 直接阈值化,调节阈值范围,建议根据图片的亮度微调范围嗷

titles = ["img","thre1"]
imgs = [img,thre1]

for i in range(2):
    plt.subplot(2,2,i+1), plt.imshow(imgs[i],"gray")  # 可以gray也可以是别的颜色啦，素材还是黑白的好
    # 推荐几个我jio得还阔以的颜色 binary YlGnBu bwr pink autumn
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])                     # 不要坐标轴啦
    # plt.xlim((0,722)),plt.ylim((722,0))             # 也可以用这个加坐标轴www
plt.show()