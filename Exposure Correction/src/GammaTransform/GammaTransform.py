'''
@program: GammaTransform.py

@description: Gamma变换核心代码

@author: doubleZ

@create: 2019/11/09
'''

import matplotlib.pyplot as plt         # plt 用于显示图片
import matplotlib.image as mpimg        # mpimg 用于读取图片


def GammaTransform(I, gamma):
    '''
    @description: 使用numpy直接对图片进行Gamma变换

    @params I: 原图
    @params gamma: Gamma变换参数

    @return : Gamma变换后的图像
    '''
    c = 255 / (255**gamma)
    J = c * I**gamma
    return J


if __name__ == '__main__':
    I = mpimg.imread('../../Resources/GammaTransform/toobright.png')
    J = GammaTransform(I, 0.5)

    plt.figure()
    plt.imshow(J, cmap='Greys_r')
    plt.axis('off')
    plt.show()
