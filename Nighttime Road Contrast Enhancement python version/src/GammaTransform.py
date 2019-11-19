'''
@program: GammaTransform.py

@description: 对图像进行Gamma变换

@author: doubleZ

@create: 2019/11/19 
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
    I = mpimg.imread('../Resources/dark_road_2.jpg')
    J = GammaTransform(I, 0.7)

    plt.figure()
    plt.imshow(J, cmap='Greys_r')
