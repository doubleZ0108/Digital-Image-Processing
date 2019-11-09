'''
@program: ProcessDarkImage.py

@description: 利用Gamma变换处理过暗灰度图像

@author: doubleZ

@create: 2019/11/09
'''


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from src.GammaTransform.GammaTransform import GammaTransform


def process_dark_image(filename):
    I = mpimg.imread(filename)

    gamma = 1
    while gamma > 0.4:
        J = GammaTransform(I, gamma)
        plt.figure()
        plt.imshow(J, cmap='Greys_r')
        gamma -= 0.1

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    process_dark_image('../../Resources/GammaTransform/toodark.png')