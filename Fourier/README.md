# Fourier变换

[TOC]

------

## 显示Fourier图像

- `imfft = abs(fft2(img))`: 进行快速傅立叶变换，处理复数幅值

- `imfftlog = log10(1 + imfft)`: 压缩最大和最小像素之间的差距

- `imfftshifted = fftshift(imfftlog)`: 将低频信号在中心点对齐

  <img src="ScreenShots/imfftlog.png" alt="imfftlog" style="zoom:50%;" />

<img src="ScreenShots/imfftshifted.png" alt="imfftshifted" style="zoom:50%;" />