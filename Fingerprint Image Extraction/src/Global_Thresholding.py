'''
@program: Global_Thresholding.py

@description: 基本全局阈值处理

@author: doubleZ

@create: 2019/12/14 
'''

import cv2 as cv
import numpy as np

def rgb2gray(img):
    '''
    :description: 将rgb图像转化为灰度图像

    :param img: 原始rgb图像

    :return : 转化后的灰度图像
    '''
    h, w = img.shape[0], img.shape[1]
    img1 = np.zeros((h,w),np.uint8)

    for i in range(h):
        for j in range(w):
            img1[i,j] = 0.144 * img[i,j,0] + 0.587 * img[i,j,1] + 0.299 * img[i,j,2]

    return img1

def threshold(img, T):
    '''
    :description: 根据当前阈值计算新阈值

    :param img: 灰度图像
    :param T: 当前的阈值

    :return : 计算得到的新阈值
    '''
    h, w = img.shape[0], img.shape[1]
    G1 = G2 = 0
    g1 = g2 = 0

    for i in range (h):
        for j in range (w):
            if img[i,j]>T:
                G1 += img[i,j]
                g1 += 1
            else:
                G2 += img[i,j]
                g2 += 1

    m1, m2 = int(G1/g1), int(G2/g2)   # m1，m2计算两组像素均值
    T0 = int((m1+m2)/2)   # 据公式计算新的阈值
    return T0

def Global_Thresholding(img, T):
    '''
    :description: 基本全局阈值处理

    :param img: 待处理图像
    :param T: 初始阈值（通常取为原图的平均灰度值，这里默认原图铺满所有像素）

    :return : 阈值处理后的图像
    '''
    h, w = img.shape[0], img.shape[1]
    img1 = np.zeros((h,w),np.uint8)
    T0 = T
    T1 = threshold(img,T0)

    for k in range (100):   # 迭代次数为经验值，可据实际情况选定
        if abs(T1-T0) == 0:   # 若新阈值减旧阈值差值为零，则为二值图最佳阈值
            for i in range (h):
                for j in range (w):
                    if img[i,j] > T1:
                        img1[i,j] = 255
                    else:
                        img1[i,j] = 0
            break
        else:
            T2 = threshold(img , T1)
            T0 = T1
            T1 = T2   # 变量转换，保证if条件为新阈值减旧阈值

    return img1

if __name__ == '__main__':
    image = cv.imread("../Resources/fingerprint.jpg")

    grayimage = rgb2gray(image)

    thresholdimage = Global_Thresholding(grayimage,127)

    cv.imshow("image", image)
    cv.imshow("grayimage", grayimage)
    cv.imshow("thresholdimage", thresholdimage)
    cv.waitKey(0)
    cv.destroyAllWindows()