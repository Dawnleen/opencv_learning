import cv2
#读取图片，以1.png为例
img=cv2.imread('D:\code\opencv_learning\opencv_learning\last\DATA1.png')
#检测关键点并计算描述
sift=cv2.xfeatures2d.SIFT_create()
#描述符是对关键点的描述，可用于图片匹配
keypoints,descriptor=sift.detectAndCompute(img,None)
#将关键点勾画到图片上
flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT
color=(0,255,0)

#参数image代表原始图片
#参数outImage是指输出在哪张图片上
#参数keypoints代表图片的关键点
#参数flags代表关键点的勾画方式
#参数color代表勾画的色彩模式
img=cv2.drawKeypoints(image=img,outImage=img,keypoints=keypoints,flags=flags,color=color)

#显示图片
cv2.imshow('sift_keypoints',img)
cv2.waitKey()