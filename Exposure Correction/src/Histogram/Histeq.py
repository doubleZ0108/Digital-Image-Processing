'''
@program: Histeq.py

@description: 对图像进行直方图均衡化

@author: doubleZ

@create: 2019/11/09 
'''
from cv2 import cv2

from src.Histogram.GenerateHistogram import generate_histogram
import numpy as np
import matplotlib.pyplot as plt


def get_histogram(img):
    '''
    @description: 计算图像的直方图信息

    @params : 图像

    @return : null
    '''
    # 建立原始图像各灰度级的灰度值与像素个数对应表
    histogram = {}
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k = img[i][j][0]
            if k in histogram:
                histogram[k] += 1
            else:
                histogram[k] = 1

    sorted_histogram = {}               # 建立排好序的映射表
    sorted_list = sorted(histogram)     # 根据灰度值进行从低至高的排序

    for j in range(len(sorted_list)):
        sorted_histogram[sorted_list[j]] = histogram[sorted_list[j]]

    return sorted_histogram


def histeq(img):
    '''
    @description: 对图像进行直方图均衡化

    @params : 图像

    @return : null
    '''
    histogram = get_histogram(img)

    pr = {}  # 建立概率分布映射表

    for i in histogram.keys():
        pr[i] = histogram[i] / (img.shape[0] * img.shape[1])

    tmp = 0
    for m in pr.keys():
        tmp += pr[m]
        pr[m] = max(histogram) * tmp

    new_img = np.zeros(shape=(img.shape[0], img.shape[1]), dtype=np.uint8)

    for k in range(img.shape[0]):
        for l in range(img.shape[1]):
            new_img[k][l] = pr[img[k][l][0]]

    return new_img


if __name__ == '__main__':
    img = cv2.imread('../../Resources/Histogram/origin.png',0)
    # new_img = histeq(img)
    new_img = cv2.equalizeHist(img)

    plt.figure()
    plt.imshow(img, cmap='Greys_r')

    plt.figure()
    plt.imshow(new_img, cmap='Greys_r')

    generate_histogram(img)
    generate_histogram(new_img)

    plt.show()