'''
@program: StandardHough.py

@description: 

@author: doubleZ

@create: 2019/12/13 
'''

import cv2
import numpy as np

# 标准霍夫变换
def StandardHough(img):
    house = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 获取灰度图
    edges = cv2.Canny(house, 50, 200)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 260)  # 霍夫变换返回的就是极坐标系中的两个参数  rho和theta
    print(np.shape(lines))
    lines = lines[:, 0, :]  # 将数据转换到二维
    for rho, theta in lines:
        a = np.cos(theta)
        b = np.sin(theta)
        # 从图b中可以看出x0 = rho x cos(theta)
        #               y0 = rho x sin(theta)
        x0 = a * rho
        y0 = b * rho
        # 由参数空间向实际坐标点转换
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv2.imshow('img', img)
    cv2.imshow('edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('../Resources/track.png')
    StandardHough(img)