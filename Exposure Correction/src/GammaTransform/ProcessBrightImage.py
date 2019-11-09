'''
@program: ProcessBrightImage.py

@description: 利用Gamma变换处理过亮灰度图像

@author: doubleZ

@create: 2019/11/09
'''


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from src.GammaTransform.GammaTransform import GammaTransform


def process_bright_image(filename):
    I = mpimg.imread(filename)

    for gamma in range(1, 6):
        J = GammaTransform(I, gamma)
        plt.figure()
        plt.imshow(J, cmap='Greys_r')

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    process_bright_image('../../Resources/GammaTransform/toobright.png')