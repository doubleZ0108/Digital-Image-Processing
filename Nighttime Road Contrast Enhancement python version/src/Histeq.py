'''
@program: Histeq.py

@description: 读图像进行直方图均衡化

@author: doubleZ

@create: 2019/11/19 
'''

import numpy as np


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
            k = img[i][j]
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
            new_img[k][l] = pr[img[k][l]]

    return new_img
