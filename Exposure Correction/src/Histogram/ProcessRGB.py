'''
@program: ProcessRGB.py

@description: 利用直方图均衡化处理rgb图像

@author: doubleZ

@create: 2019/11/10 
'''

from cv2 import cv2
from src.Histogram.GenerateHistogram import generate_histogram
from src.Histogram.Histeq import histeq
import matplotlib.pyplot as plt


def show_rgb(img):
    '''
    @description: 将bgr格式图像转换为rgb图像并显示

    @params : bgr格式对图像

    @return : null
    '''
    b, g, r = cv2.split(img)
    img_rgb = cv2.merge([r, g, b])
    plt.figure()
    plt.imshow(img_rgb)
    plt.show()


def main():
    I = cv2.imread('../../Resources/Histogram/rgb_figure2.png')

    # 提取rgb图像的三通道 => 分别进行直方图均衡化 => 合并成rgb图像
    bI, gI, rI = cv2.split(I)
    # bJ, gJ, rJ = histeq(bI), histeq(gI), histeq(rI)
    bJ, gJ, rJ = cv2.equalizeHist(bI), cv2.equalizeHist(gI), cv2.equalizeHist(rI)
    J = cv2.merge([bJ, gJ, rJ])


    show_rgb(I)
    show_rgb(J)


if __name__ == '__main__':
    main()