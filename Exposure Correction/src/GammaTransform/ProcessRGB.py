'''
@program: ProcessRGB.py

@description: 利用Gamma变换处理rgb图像

@author: doubleZ

@create: 2019/11/09
'''


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from src.GammaTransform.GammaTransform import GammaTransform
import numpy as np

def process_rgb(filename):
    I = mpimg.imread(filename)
    plt.figure()
    plt.imshow(I)

    # 提取三通道像素信息
    rI, gI, bI = I[:, :, 0], I[:, :, 1], I[:, :, 2]

    # 设置gamma的三个分量值
    gamma_r, gamma_g, gamma_b = 1, 1, 1
    rJ, gJ, bJ = GammaTransform(rI, gamma_r), GammaTransform(gI, gamma_g), GammaTransform(bI, gamma_b)

    # 将三个通道进行深度组合
    J = np.dstack((rJ, gJ, bJ))
    plt.figure()
    plt.imshow(J)

    # plt.axis('off')
    plt.show()


if __name__ == '__main__':
    process_rgb('../../Resources/GammaTransform/rgb_figure2.png')
