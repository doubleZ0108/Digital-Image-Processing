'''
@program: ProgressiveProbability_Hough.py

@description: 渐进概率式霍夫变换提取机场跑道线

@author: doubleZ

@create: 2019/12/13 
'''

import cv2
import numpy as np

def ProgressiveProbability_Hough(img):
    '''
    :description: 渐进概率式霍夫变换

    :param : 原始图像

    :return : 显示用渐进概率式霍夫变换提取的直线边缘图像
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 250)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, minLineLength=60, maxLineGap=10)
    lines = lines[:, 0, :]
    for x1, y1, x2, y2 in lines:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('../Resources/track.png')
    ProgressiveProbability_Hough(img)