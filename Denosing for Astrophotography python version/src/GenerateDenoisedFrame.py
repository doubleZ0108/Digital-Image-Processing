'''
@program: GenerateDenoisedFrame.py

@description: 对视频对帧进行平滑去噪

@author: doubleZ

@create: 2019/11/11 
'''

import pylab
import imageio
import skimage
import numpy as np

def show_frame(frame, name):
    '''
    @description: 绘制帧

    @params frame: 帧数据ndaray
    @params name: 图像对名字

    @return : null
    '''
    img_now = pylab.figure()
    img_now.suptitle(name)
    pylab.imshow(frame)


def denoise_for_video():
    # 视频的相对路径
    filename = '../Resources/hw1_sky_1.avi'

    # 选择ffmpeq作为解码工具
    vidobj = imageio.get_reader(filename, 'ffmpeg')

    # 提取视频对各帧并进行去噪处理
    for t, frame_now in enumerate(vidobj):
        if t == 0:  # 读取第一帧
            frame_average_last = skimage.img_as_float(frame_now).astype(np.float64)
            continue

        frame_now = skimage.img_as_float(frame_now).astype(np.float64)  # 提取下一帧
        frame_average = (t - 1) / t * frame_average_last + 1 / t * frame_now  # 将之前对处理结果和现有帧加权求和
        frame_average_last = frame_average  # 更新处理结果

    return [frame_now, frame_average]


def main():
    [frame_now, frame_average] = denoise_for_video()

    show_frame(frame_now, "frame now")
    show_frame(frame_average, "frame average")

    pylab.show()


if __name__ == '__main__':
    main()
