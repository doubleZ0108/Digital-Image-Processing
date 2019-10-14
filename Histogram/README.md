# 直方图 | Histogram

[TOC]

------

## 直方图计算 | Histogram Computation

- **公式：**

$$
h(r_k) = n_k, \ \ r_k：第k个灰度级 \  n_k：灰度级位rk的像素数
$$

- **库函数：**

  ```matlab
  imhist(I);
  ```

  <img src="ScreenShots/Histogram_Computation.png" alt="Histogram_Computation" style="zoom:50%;" />

------

## 直方图均衡化 | Histogram Equalization

- **公式：**
  $$
  s = (L - 1)\sum_{j=0}^{k}\frac{n_j}{M*N} \\ \\ L为总灰度级 \\ M*N为图像尺寸 \\ n_j为直方图中第j项的值
  $$
  再将原图中的灰度转换为新图像中的灰度级

**原图**

<img src="ScreenShots/origin.png" alt="origin" style="zoom:80%;" />

**直方图均衡化**

<img src="ScreenShots/result.png" alt="result" style="zoom:80%;" />

**前后直方图对比**

<img src="ScreenShots/histogram1.png" alt="histogram1" style="zoom:80%;" />

**原图**

<img src="ScreenShots/origin2.png" alt="origin2" style="zoom: 50%;" />

**直方图均衡化**

<img src="ScreenShots/result2.png" alt="result2" style="zoom:50%;" />

**前后直方图对比**

<img src="ScreenShots/histogram2.png" alt="histogram2" style="zoom:80%;" />