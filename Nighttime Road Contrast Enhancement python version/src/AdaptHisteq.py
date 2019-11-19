'''
@program: AdaptHisteq.py

@description: 

@author: doubleZ

@create: 2019/11/19 
'''
import numpy as np
import cv2


def adapthisteq(I, cliplimit=2.0, tilegridsize=(8,8)):
    '''
    @description: 对原图进行自适应直方图均衡化

    @params I: 原图
    @params cliplimit: 指定直方图均衡化的限幅(默认为2.0)
    @params tilegridsize: 指定自适应直方图均衡化的瓦片大小(默认为8*8的瓦片)

    @return : 自适应直方图均衡化后的图像
    '''


    # 进行正规化
    I_max = np.amax(I)
    I_min = np.amin(I)
    I_img = ((I - I_min) / (I_max - I_min)) * 255
    I_img = I_img.astype('uint8')

    clahe = cv2.createCLAHE(clipLimit=cliplimit, tileGridSize=tilegridsize)
    J = clahe.apply(I)

    return J
