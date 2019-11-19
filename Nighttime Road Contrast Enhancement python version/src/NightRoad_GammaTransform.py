'''
@program: NightRoad_GammaTransform.py

@description: 使用Gamma变换对夜间监控摄像头图像进行增强.

@author: doubleZ

@create: 2019/11/19 
'''
import matplotlib.pyplot as plt         # plt 用于显示图片
import matplotlib.image as mpimg        # mpimg 用于读取图片
from src.GammaTransform import GammaTransform


def main():
    dir_name = '../Resources/'
    imgs_name = ['dark_road_1.jpg', 'dark_road_2.jpg', 'dark_road_3.jpg']

    for img_name in imgs_name:
        I = mpimg.imread(dir_name + img_name)
        J = GammaTransform(I, 0.7)

        plt.figure()
        plt.imshow(I, cmap='Greys_r')

        plt.figure()
        plt.imshow(J, cmap='Greys_r')

    plt.show()


if __name__ == '__main__':
    main()