import cv2
import numpy as np

# pyrDown():brief Blurs an image and downsamples it.
# 将图像高斯平滑，然后进行降采样
img = cv2.pyrDown(cv2.imread(r'D:\code\opencv_learning\opencv_learning\last\DATA1.png', cv2.IMREAD_UNCHANGED))
# 依然是二值化操作
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
# 计算图像的轮廓
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # find bounding box coordinates
    # 先计算出一个简单的边界狂，也就是一个矩形啦
    # 就是将轮廓信息转换为(x,y)坐标，并加上矩形的高度和宽度
    x, y, w, h = cv2.boundingRect(c)
    # 画出该矩形
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # find minimum area
    # 然后计算包围目标的最小矩形区域
    # 这里先计算出最小矩形区域，然后计算区域的顶点，此时顶点坐标是浮点型，但是像素坐标是整数
    # 需要将浮点型转换成矩形
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    # draw contours
    # 画出最小矩形
    # drawContours()也会修改源图像
    # 第二个参数保存轮廓的数组，也就是保存着很多轮廓
    # 第三个参数是要绘制的轮廓数组的索引：-1是绘制所有的轮廓，否则只绘制[box]中指定的轮廓
    # 颜色和thickness(密度,就是粗细)放在最后两个参数
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    # calculate center and radius of minimum enclosing circle
    # 最后检查的边界轮廓为最小闭圆
    # minEnclosingCircle()会返回一个二元数组，第一个是圆心坐标组成的元祖，第二个元素是元的半径
    (x, y), radius = cv2.minEnclosingCircle(c)
    # cast to integers
    center = (int(x), int(y))
    radius = int(radius)
    # draw the circle
    img = cv2.circle(img, center, radius, (255, 0, 0), 3)

# 绘制轮廓
cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()
