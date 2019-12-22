# 噪声类型



[TOC]

------

**原图**

<img src="Resources/origin.png" alt="demo" style="zoom:50%;" />

<img src="ScreenShots/origin_histogram.png" alt="origin_histogram" style="zoom:50%;" />

------

## Gaussian | 高斯

<img src="ScreenShots/gaussian.png" alt="gaussian" style="zoom: 50%;" />

<img src="ScreenShots/gaussian_histogram.png" alt="gaussian_histogram" style="zoom:50%;" />

------

## Poisson | 柏松

<img src="ScreenShots/poisson.png" alt="poisson" style="zoom:50%;" />

<img src="ScreenShots/poisson_histogram.png" alt="poisson_histogram" style="zoom:50%;" />

------

## Rayleigh | 瑞利



------

## Erlang(Gamma) | 爱尔兰



------

## Exponential | 指数



------

## Uniform | 均匀



------

## Impulse | 脉冲

### Salt & pepper noise | 椒盐

<img src="ScreenShots/salt_and_pepper.png" alt="salt_and_pepper" style="zoom:50%;" />

<img src="ScreenShots/salt_pepper_histogram.png" alt="salt_pepper_histogram" style="zoom:50%;" />

------

## Speckle | 斑点噪声

<img src="ScreenShots/speckle.png" alt="speckle" style="zoom:50%;" />

<img src="ScreenShots/speckle_histogram.png" alt="speckle_histogram" style="zoom:50%;" />

------

## 周期噪声

- 由于电子元件，会产生周期噪声
- 正弦波的傅立叶变换是位于正弦波共轭频率处的一堆共轭脉冲
- 图像叠加了周期噪声，转换到频域会产生明显的白点
- 可以通过频域滤波显著消除