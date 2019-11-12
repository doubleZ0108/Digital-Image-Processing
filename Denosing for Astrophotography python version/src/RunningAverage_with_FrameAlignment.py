'''
@program: RunningAverage_with_FrameAlignment.py

@description: 

@author: doubleZ

@create: 2019/11/11 
'''

import pylab
import imageio
import skimage
import numpy as np
from cv2 import cv2


def imshift(frame, dx, dy):
    M, N = frame.shape[:2]
    A = np.float32([[1, 0, dx], [0, 1, dy]])
    shifted_frame = cv2.warpAffine(frame, A, (N, M))
    return shifted_frame

def Align(f, g):
    M, N = f.shape[:2]
    diff = (f - g)**2
    min_msd = np.sum(np.reshape(diff, (diff.size,))) / (M * N)
    min_msd_frame = f
    min_index = [0, 0]

    n = 10
    for dx in range(-n, n):
        for dy in range(-n, n):
            shifted_f = imshift(f, dx, dy)

            M, N, type = f.shape[:3]
            rowl, rowr = 0, M+dy-1
            colt, colb = dx, N
            if rowr > M:
                rowr = M - 1
            if colt < 1:
                colt = 0

            sub_f = shifted_f[rowl:rowr, colt:colb]
            sub_g = g[rowl:rowr, colt:colb]
            # sub_f = shifted_f
            # sub_g = g

            diff = (sub_f - sub_g) ** 2
            M, N = sub_f.shape[:2]
            msd = np.sum(np.reshape(diff, (diff.size,))) / (M * N)

            if msd < min_msd:
                min_msd = msd
                min_msd_frame = shifted_f
                min_index = [dx, dy]
    return min_msd_frame



if __name__ == '__main__':
    # 视频的绝对路径
    filename = '../Resources/hw1_sky_1.avi'

    # 可以选择解码工具
    vidobj = imageio.get_reader(filename, 'ffmpeg')

    for t, frame_now in enumerate(vidobj):
        print(t)
        if t == 0:    # 读取第一帧
            frame_average_last = skimage.img_as_float(frame_now).astype(np.float64)
            continue
        frame_now = skimage.img_as_float(frame_now).astype(np.float64)  # 提取下一帧
        frame_average = (t - 1) / t * frame_average_last + 1 / t * Align(frame_now, frame_average_last);
        frame_average_last = frame_average;


    img_now = pylab.figure()
    img_now.suptitle('frame now')
    pylab.imshow(frame_now)

    img_average = pylab.figure()
    img_average.suptitle('frame average')
    pylab.imshow(frame_average)
    pylab.show()
