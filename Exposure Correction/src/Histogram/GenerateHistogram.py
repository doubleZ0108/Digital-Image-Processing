'''
@program: GenerateHistogram.py

@description: 绘制图像的直方图

@author: doubleZ

@create: 2019/11/09 
'''

import matplotlib.pyplot as plt
import numpy as np
import cv2


def generate_histogram(img):
    '''
    @description: 用定义法生成图像的直方图

    @params img: 图像（二维矩阵）

    @return : null
    '''
    height, width = img.shape[:2]
    histogram = np.zeros([256])
    for i in range(height):
        for j in range(width):
            histogram[img[i][j]] += 1

    x = np.arange(256)
    plt.figure()
    plt.plot(x, histogram, 'r', linewidth=2, c='black')
    plt.show()


def generate_histogram_library(img):
    '''
    @description: 用库函数生成图像的直方图

    @params img: 图像（二维矩阵）

    @return : null
    '''
    img_arr = img.flatten()     # 现将原图片转化为一维向量的形式
    plt.figure("hist")
    n, bins, patches = plt.hist(img_arr, bins=256, facecolor='blue', alpha=0.75)
    plt.show()


if __name__ == '__main__':
    img = cv2.imread('../../Resources/Histogram/origin.png', cv2.IMREAD_GRAYSCALE)
    generate_histogram(img)
    generate_histogram_library(img)

