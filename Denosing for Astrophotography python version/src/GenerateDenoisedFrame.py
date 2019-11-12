'''
@program: GenerateDenoisedFrame.py

@description: 

@author: doubleZ

@create: 2019/11/11 
'''

import pylab
import imageio
import skimage
import numpy as np


if __name__ == '__main__':
    # 视频的绝对路径
    filename = '../Resources/hw1_sky_1.avi'

    # 可以选择解码工具
    vidobj = imageio.get_reader(filename, 'ffmpeg')

    for t, frame_now in enumerate(vidobj):
        if t == 0:    # 读取第一帧
            frame_average_last = skimage.img_as_float(frame_now).astype(np.float64)
            continue
        frame_now = skimage.img_as_float(frame_now).astype(np.float64)  # 提取下一帧
        frame_average = (t - 1) / t * frame_average_last + 1 / t * frame_now  # weighted summation
        frame_average_last = frame_average  # update the fresh frame


    img_now = pylab.figure()
    img_now.suptitle('frame now')
    pylab.imshow(frame_now)

    img_average = pylab.figure()
    img_average.suptitle('frame average')
    pylab.imshow(frame_average)
    pylab.show()
