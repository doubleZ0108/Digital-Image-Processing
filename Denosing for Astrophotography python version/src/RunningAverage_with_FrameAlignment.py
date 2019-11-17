'''
@program: RunningAverage_with_FrameAlignment.py

@description: 对帧视频进行平滑操作，并且进行图像增强

@author: doubleZ

@create: 2019/11/11 
'''

import pylab
import imageio
import skimage
import numpy as np
from cv2 import cv2
from src.ShowFrame import show_frame



def imshift(frame, dx, dy):
    '''
    @description: 将图像向右平移dx像素，向下平移dy像素

    @params dx: 向右的步长
    @param dy: 向下的步长

    @return : 平移后的图像
    '''
    M, N = frame.shape[:2]
    A = np.float32([[1, 0, dx], [0, 1, dy]])
    shifted_frame = cv2.warpAffine(frame, A, (N, M))
    return shifted_frame


def Align(f, g):
    '''
    @description: 校准两张图像，获得最好的对齐效果

    @params f: 待校准图像一
    @params g: 待校准图像二

    @return : 校准后对图像
    '''
    M, N = f.shape[:2]
    diff = (f - g)**2       # 原始两张图像的差异
    min_msd = np.sum(np.reshape(diff, (diff.size,))) / (M * N)  # 使用欧拉距离抽象该差异的大小
    min_msd_frame = f       # 初始化校准图像为原图像
    min_index = [0, 0]      # 初始化不需要进行平移图像

    n = 10     # 这个参数用于控制比较的范围，n越大，获得的效果越好，但是同样计算的时间也越长

    for dx in range(-n, n):
        for dy in range(-n, n):
            shifted_f = imshift(f, dx, dy)  # 将待校准图像一进行平移

            # 裁剪原图像以对齐
            M, N, type = f.shape[:3]
            rowl, rowr = 0, M+dy-1
            colt, colb = dx, N
            if rowr > M:
                rowr = M - 1
            if colt < 1:
                colt = 0

            sub_f = shifted_f[rowl:rowr, colt:colb]
            sub_g = g[rowl:rowr, colt:colb]

            diff = (sub_f - sub_g) ** 2     # 重新计算两张图像的差异
            M, N = sub_f.shape[:2]
            msd = np.sum(np.reshape(diff, (diff.size,))) / (M * N)  # 再次用欧拉距离抽象

            if msd < min_msd:       # 如果差异更小（代表该校准图像更好），则更新校准图像
                min_msd = msd
                min_msd_frame = shifted_f
                min_index = [dx, dy]
    return min_msd_frame


def main():
    # 视频的绝对路径
    filename = '../Resources/sky_1.avi'

    # 可以选择解码工具
    vidobj = imageio.get_reader(filename, 'ffmpeg')

    for t, frame_now in enumerate(vidobj):
        print(t)
        if t == 0:  # 读取第一帧
            frame_average_last = skimage.img_as_float(frame_now).astype(np.float64)
            continue
        frame_now = skimage.img_as_float(frame_now).astype(np.float64)  # 提取下一帧
        frame_average = (t - 1) / t * frame_average_last + 1 / t * Align(frame_now, frame_average_last)
        frame_average_last = frame_average

    show_frame(frame_now, 'frame now')

    show_frame(frame_average, 'frame average with align')

    pylab.show()


if __name__ == '__main__':
    main()