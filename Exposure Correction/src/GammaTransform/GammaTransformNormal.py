'''
@program: GammaTransformNormal.py

@description: Gamma变换核心代码（初级版）

@author: doubleZ

@create: 2019/11/09
'''

import matplotlib.pyplot as plt         # plt 用于显示图片
import matplotlib.image as mpimg        # mpimg 用于读取图片
import numpy as np

def GammaTransform_each_pixel(I, gamma):
    '''
    @description: 逐像素的进行Gamma变换

    @params I: 原图
    @params gamma: Gamma变换参数

    @return : Gamma变换后的图像
    '''
    M, N = I.shape[0], I.shape[1]       # 获取原始图像的尺寸
    J = np.zeros((M, N))                 # 新建与原图同尺寸的空白图片

    c = 255 / (255 ** gamma)

    '''逐像素的进行Gamma变换'''
    for i in range(M):
        for j in range(N):
            J[i][j] = c * I[i][j]**gamma

    return J


if __name__ == '__main__':
    I = mpimg.imread('../../Resources/GammaTransform/toodark.png')
    J = GammaTransform_each_pixel(I, 2)

    plt.figure()
    plt.imshow(J, cmap='Greys_r')

    plt.axis('off') # 不显示坐标轴
    plt.show()
