'''
@program: NightRoad_Adapthisteq.py

@description: 使用自适应直方图均衡化对夜间监控摄像头图像进行增强.

@author: doubleZ

@create: 2019/11/19 
'''

import matplotlib.pyplot as plt         # plt 用于显示图片
import matplotlib.image as mpimg        # mpimg 用于读取图片
from src.AdaptHisteq import adapthisteq

def main():
    dir_name = '../Resources/'
    imgs_name = ['dark_road_1.jpg', 'dark_road_2.jpg', 'dark_road_3.jpg']

    cliplimit, tilegridsize = 2.0, (8, 8)

    for img_name in imgs_name:
        I = mpimg.imread(dir_name + img_name)

        J = adapthisteq(I)


        plt.figure()
        plt.imshow(I, cmap='Greys_r')

        plt.figure()
        plt.imshow(J, cmap='Greys_r')

        I_arr = I.flatten()
        plt.figure()
        n, bins, patches = plt.hist(I_arr, bins=256, density=1, edgecolor='None', facecolor='blue')
        plt.show()
        J_arr = J.flatten()
        plt.figure()
        n, bins, patches = plt.hist(J_arr, bins=256, density=1, edgecolor='None', facecolor='blue')
        plt.show()


    plt.show()


if __name__ == '__main__':
    main()