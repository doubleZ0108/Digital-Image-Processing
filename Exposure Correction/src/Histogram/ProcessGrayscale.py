'''
@program: ProcessGrayscale.py

@description: 利用直方图均衡化处理灰度图

@author: doubleZ

@create: 2019/11/10 
'''
from cv2 import cv2, IMREAD_GRAYSCALE
from src.Histogram.GenerateHistogram import generate_histogram
from src.Histogram.Histeq import histeq
import matplotlib.pyplot as plt


def main():
    img = cv2.imread('../../Resources/Histogram/origin.png', IMREAD_GRAYSCALE)


    # 自定义算法
    new_img = histeq(img)

    # 库函数
    # new_img = cv2.equalizeHist(img)

    plt.figure()
    plt.imshow(img, cmap='Greys_r')

    plt.figure()
    plt.imshow(new_img, cmap='Greys_r')

    # 显示直方图
    # generate_histogram(img)
    # generate_histogram(new_img)

    plt.show()


if __name__ == '__main__':
    main()