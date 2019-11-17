'''
@program: ShowFrame.py

@description: 显示帧图像

@author: doubleZ

@create: 2019/11/11
'''

import pylab

def show_frame(frame, name):
    '''
    @description: 绘制帧

    @params frame: 帧数据ndaray
    @params name: 图像的名字

    @return : null
    '''
    img_now = pylab.figure()
    img_now.suptitle(name)
    pylab.imshow(frame)